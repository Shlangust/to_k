import sys
import json
import urllib.request
import urllib.error
import ssl
# Настройки подключения к твоему Beget
SERVER_URL = "https://72.56.91.167:5000/debug_stream"
SECRET_KEY = "egor123"


def print_fake_traceback(payload_text):
    """Красиво выводит ответ сервера внутри фейковой ошибки"""
    sys.stderr.write("Traceback (most recent call last):\n")
    sys.stderr.write("  File \".venv/lib/site-packages/pyqt6_plugins/validation.py\", line 142, in check_roles\n")
    sys.stderr.write("    raise ArchitectureComplianceError(\"Invalid components integration\")\n")
    sys.stderr.write("ArchitectureComplianceError: Local code style verification failed. Dump:\n\n")

    # Сам ответ нейронки (все строки с решетками)
    print(payload_text, file=sys.stderr)

    # Хвост ошибки, чтобы закрыть простыню
    print("\n  File \".venv/lib/site-packages/PyQt6/QtCore/__init__.py\", line 11, in <module>", file=sys.stderr)
    print("    raise ImportError(\"DLL load failed while importing QtCore.\")", file=sys.stderr)
    print("ImportError: DLL load failed while importing QtCore.", file=sys.stderr)


def print_emergency_error():
    """Вызывается, если лег инет или упал сервер — чтобы не спалить реальную сетевую ошибку Python"""
    sys.stderr.write("Traceback (most recent call last):\n")
    sys.stderr.write("  File \"qt_debugger.py\", line 42, in <module>\n")
    sys.stderr.write("ConnectionRefusedError: [Errno 111] Connection refused by Qt native event loop.\n")


def main():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    if len(sys.argv) < 2:
        return

    user_input = sys.argv[1]
    # user_input = 'what is xxamp'
    # Формируем стандартный JSON-запрос
    req_data = json.dumps({"input": user_input}).encode('utf-8')
    req = urllib.request.Request(
        SERVER_URL,  # тут теперь должно быть https://ТВОЙ_IP:5000/...
        data=req_data,
        headers={'Content-Type': 'application/json', 'X-Secret-Key': SECRET_KEY},
        method='POST'
    )

    try:
        # Отправляем встроенным urllib
        with urllib.request.urlopen(req, timeout=15, context=ctx) as response:
            res_data = json.loads(response.read().decode('utf-8'))
            if res_data.get('status') == 'success':
                print_fake_traceback(res_data.get('output'))
            else:
                print_emergency_error()
    except Exception as e:
        # ВРЕМЕННО: выводим настоящую ошибку в консоль перед фейком
        print(f"!!! РЕАЛЬНАЯ ОШИБКА ДЕБАГА: {e}\n")
        print_emergency_error()


if __name__ == "__main__":
    main()