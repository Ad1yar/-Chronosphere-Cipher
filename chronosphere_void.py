import base64

class ChronosphereCipher:
    def __init__(self, key: str):
        self.key_bytes = key.encode('utf-8')
        
    def _manipulate_time(self, data: bytes) -> bytes:
        result = bytearray()
        key_len = len(self.key_bytes)
        
        for i, byte in enumerate(data):
            key_byte = self.key_bytes[i % key_len]
            # Динамический сдвиг на основе позиции символа и ключа
            time_shift = (i * 7 + key_byte) % 256
            transformed_byte = byte ^ key_byte ^ time_shift
            result.append(transformed_byte)
            
        return bytes(result)

    def encrypt(self, text: str) -> str:
        raw_bytes = text.encode('utf-8')
        encrypted_bytes = self._manipulate_time(raw_bytes)
        return base64.b64encode(encrypted_bytes).decode('utf-8')

    def decrypt(self, encrypted_text: str) -> str:
        try:
            encrypted_bytes = base64.b64decode(encrypted_text.encode('utf-8'))
            decrypted_bytes = self._manipulate_time(encrypted_bytes)
            return decrypted_bytes.decode('utf-8')
        except Exception:
            return "[Ошибка]: Купол схлопнулся! Неверный ключ или поврежденные данные."


def main():
    print("=" * 45)
    print("      CHRONOSPHERE CIPHER (Faceless Void)     ")
    print("=" * 45)

    key = input("Задай секретный ключ (пароль): ").strip()
    if not key:
        print("Ключ не может быть пустым!")
        return

    cipher = ChronosphereCipher(key)

    while True:
        print("\nВыбери действие:")
        print("1. Зашифровать текст")
        print("2. Расшифровать текст")
        print("3. Выйти")
        
        choice = input("Твой выбор (1/2/3): ").strip()

        if choice == "1":
            user_text = input("\nВведи текст для зашифровки: ")
            encrypted = cipher.encrypt(user_text)
            print(f"\nЗашифрованный текст (скопируй его):\n{encrypted}")
            
        elif choice == "2":
            encrypted_text = input("\nВведи зашифрованный текст: ")
            decrypted = cipher.decrypt(encrypted_text)
            print(f"\nРезультат:\n{decrypted}")
            
        elif choice == "3":
            print("\nВойд ушел в астрал.")
            break
        else:
            print("Неверный выбор, попробуй еще раз.")

if __name__ == "__main__":
    main()