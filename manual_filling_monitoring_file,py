
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os
from threading import Timer


class DebouncedWatcher(FileSystemEventHandler):
   def __init__(self):
       self.pending_notifications = {}
       self.debounce_interval = 2  # секунды
       self.from_email = input("Введите ваш Gmail адрес (отправитель): ").strip()
       self.app_password = input("Введите пароль приложения Gmail: ").strip()
       self.to_email = input("Введите email получателя: ").strip()
      
       print(f"\nНастройки email:")
       print(f"Отправитель: {self.from_email}")
       print(f"Получатель: {self.to_email}")
       print(f"Debounce интервал: {self.debounce_interval} сек\n")
  
   def debounce_notification(self, key, change_description):
       """Откладывает отправку уведомления для группировки быстрых изменений"""
       if key in self.pending_notifications:
           self.pending_notifications[key].cancel()
      
       timer = Timer(self.debounce_interval, self.send_email_notification, [change_description])
       self.pending_notifications[key] = timer
       timer.start()
  
   def send_email_notification(self, change_description):
       """Отправляет уведомление на почту об изменении"""
       try:
           msg = MIMEMultipart()
          
           msg['Subject'] = f"Файловые изменения: {change_description[:50]}..." 
           msg['From'] = self.from_email
           msg['To'] = self.to_email


           msg_body = f"""Обнаружено изменение в файловой системе:


{change_description}


Время обнаружения: {time.strftime('%Y-%m-%d %H:%M:%S')}
Система: {os.name}
"""
           msg.attach(MIMEText(msg_body, 'plain'))


           server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
           server.login(self.from_email, self.app_password)
           server.sendmail(self.from_email, self.to_email, msg.as_string())
           server.quit()
          
           print(f"✓ Уведомление отправлено: {change_description}")
          
       except smtplib.SMTPAuthenticationError:
           print("❌ Ошибка аутентификации. Проверьте email и пароль приложения")
       except Exception as e:
           print(f"❌ Ошибка при отправке email: {e}")


   def on_modified(self, event):
       if event.is_directory:
           return
      
       change_description = f"Изменен файл: {event.src_path}"
       print(f"📝 {change_description}")
       # Используем путь файла как ключ для дебаунса
       self.debounce_notification(f"modified_{event.src_path}", change_description)


   def on_created(self, event):
       if event.is_directory:
           return
      
       change_description = f"Создан файл: {event.src_path}"
       print(f"🆕 {change_description}")
       # Используем путь файла как ключ для дебаунса
       self.debounce_notification(f"created_{event.src_path}", change_description)


   def on_deleted(self, event):
       if event.is_directory:
           return
      
       change_description = f"Удален файл: {event.src_path}"
       print(f"🗑️ {change_description}")
       # Для удаленных файлов используем другой ключ
       self.debounce_notification(f"deleted_{event.src_path}", change_description)


   def on_moved(self, event):
       if event.is_directory:
           return
      
       change_description = f"Файл перемещен: {event.src_path} → {event.dest_path}"
       print(f"➡️ {change_description}")
       # Для перемещения используем исходный путь как ключ
       self.debounce_notification(f"moved_{event.src_path}", change_description)


def get_monitoring_path():
   """Запрашивает путь для мониторинга у пользователя"""
   default_path = "/home/igrami/Загрузки"
   path = input(f"Введите путь для мониторинга (по умолчанию: {default_path}): ").strip()
  
   if not path:
       path = default_path
  
   if not os.path.exists(path):
       print(f"❌ Путь '{path}' не существует!")
       return None
  
   return path


def main():
   print("=== File System Monitor ===")
   print("Система мониторинга файлов с email уведомлениями\n")
  
   # Получаем путь для мониторинга
   monitoring_path = get_monitoring_path()
   if not monitoring_path:
       return
  
   print(f"\n🛠️ Инициализация наблюдателя...")
  
   # Создаем и запускаем наблюдатель
   event_handler = DebouncedWatcher()
   observer = Observer()
   observer.schedule(event_handler, path=monitoring_path, recursive=True)


   print(f"✅ Мониторинг запущен для: {monitoring_path}")
   print("Нажмите Ctrl+C для остановки...\n")


   try:
       observer.start()
       while True:
           time.sleep(1)
   except KeyboardInterrupt:
       print("\n🛑 Остановка мониторинга...")
       observer.stop()
      
       # Отменяем все ожидающие таймеры
       for timer in event_handler.pending_notifications.values():
           timer.cancel()
  
   observer.join()
   print("✅ Мониторинг завершен")


if __name__ == '__main__':
   main()
