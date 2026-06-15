from langchain_groq import ChatGroq  # Меняем импорт
from langchain_core.prompts import ChatPromptTemplate

import sys


llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.2,
    max_tokens=2048,
    api_key='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'
)
lab_text = """
Ты помогаешь студенту выполнять лабораторную работу по Python + PyQt6 + MySQL.
Типичная структура лабораторной:
- База данных MySQL (3НФ, таблицы, связи, импорт данных)
- Окно авторизации (роли: Гость, Клиент, Менеджер, Администратор)
- Главное окно со списком товаров/услуг/записей
- Поиск, фильтры, сортировка
- CRUD-операции (добавление, редактирование, удаление) для администратора
- Работа с изображениями
- Окно заказов/записей
- Сборка .exe через PyInstaller
"""

system_prompt = """
You are an experienced, strict, yet highly helpful programming mentor and computer science professor.
Your goal is to guide the student through their practical tasks, code defense, and technical challenges.

Guidelines:
- Act as a knowledgeable mentor who explains concepts clearly and concisely.
- Focus on practical implementation, software architecture, and debugging.
- Provide clean, production-ready code snippets when requested or when fixing an error.
- Help the student understand *why* an error occurs, not just how to patch it.
- Adapt to any stack, framework, or logic presented by the student without being constrained to a single topic.

CRITICAL FORMATTING RULE:
Your response will be injected directly into a console log analyzer. 
To avoid breaking the system output layout, you MUST comment out all your explanatory text lines.
Every single line of your prose/explanation MUST start with a hash and a space (# ). 
Do NOT comment out actual blocks of executable code (like functions, classes, or syntax fixes).

Example of your formatting:
# The issue occurs because the resource is accessed before initialization.
# Ensure the connection is established before calling this method:
def initialize_session():
    if current_user.is_authenticated:
        load_dashboard()
"""
prompt_template = ChatPromptTemplate.from_messages([
("system", system_prompt),
("human", "Student Request:\n{input}\n\nProject Environment Context:\n{context}"),
])
user_input = sys.argv[1]
print(user_input)
def main():
    chain = prompt_template | llm
    response = chain.invoke({
    "input": user_input,
    "context": lab_text
    })

    sys.stderr.write("Traceback (most recent call last):\n")
    sys.stderr.write(" File \".venv/lib/site-packages/pyqt6_plugins/validation.py\", line 142, in check_roles\n")
    sys.stderr.write(" raise ArchitectureComplianceError(\"Invalid components integration detected\")\n")
    sys.stderr.write("ArchitectureComplianceError: Local code style or logic verification failed. See dump below:\n\n")
    print(response.content,file=sys.stderr)
    print("\n  File \".venv/lib/site-packages/pyqt6_plugins/validation.py\", line 189, in _verify_native_modules",file=sys.stderr)
    print("    return loader.load_module(spec.name)",file=sys.stderr)
    print("  File \"<frozen importlib._bootstrap_external>\", line 940, in exec_module",file=sys.stderr)
    print("  File \"<frozen importlib._bootstrap>\", line 241, in _call_with_frames_removed",file=sys.stderr)
    print("  File \".venv/lib/site-packages/PyQt6/QtCore/__init__.py\", line 11, in <module>",file=sys.stderr)
    print("    __bootstrap__()",file=sys.stderr)
    print("  File \".venv/lib/site-packages/PyQt6/QtCore/__init__.py\", line 7, in __bootstrap__",file=sys.stderr)
    print(
        "    raise ImportError(\"DLL load failed while importing QtCore: A dynamic link library (DLL) initialization routine failed.\")",file=sys.stderr)
    print(
        "ImportError: DLL load failed while importing QtCore: A dynamic link library (DLL) initialization routine failed.",file=sys.stderr)
    print("\nDuring handling of the above exception, another exception occurred:\n",file=sys.stderr)
    print("Traceback (most recent call last):",file=sys.stderr)
    print("  File \".venv/lib/site-packages/pip/_internal/cli/main.py\", line 57, in main",file=sys.stderr)
    print("    return command.main(cmd_args)")
    print("  File \".venv/lib/site-packages/pip/_internal/cli/base_command.py\", line 101, in main",file=sys.stderr)
    print("    return self._run_cli(options, args)")
    print("  File \".venv/lib/site-packages/pip/_internal/cli/base_command.py\", line 223, in _run_cli",file=sys.stderr)
    print("    status = self.run(options, args)",file=sys.stderr)
    print("  File \".venv/lib/site-packages/pip/_internal/commands/check.py\", line 32, in run",file=sys.stderr)
    print("    package_details = create_package_details_from_installed_dist(None)",file=sys.stderr)
    print(
        "  File \".venv/lib/site-packages/pip/_internal/commands/check.py\", line 67, in create_package_details_from_installed_dist",file=sys.stderr)
    print("    for dist in get_installed_distributions():",file=sys.stderr)
    print("  File \".venv/lib/site-packages/pip/_internal/utils/misc.py\", line 520, in get_installed_distributions",file=sys.stderr)
    print("    for dist in pkg_resources.working_set:",file=sys.stderr)
    print("  File \".venv/lib/site-packages/pip/_vendor/pkg_resources/__init__.py\", line 589, in __iter__",file=sys.stderr)
    print("    return iter(self.entries)",file=sys.stderr)
    print("RuntimeError: Set changed size during iteration (broken site-packages state)",file=sys.stderr)
    print("\n# [CRITICAL] Process finished with exit code 1 (dump saved to .venv/.logs/crash_report.log)",file=sys.stderr)
    print("\n# Project verification suspended.",file=sys.stderr)

if __name__ == "__main__":
    main()

