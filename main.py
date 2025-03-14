import sys

from netrapier.constants import VERSION, AUTHOR, LINK
from netrapier import NetRapierWindow

from PySide6.QtWidgets import QApplication


def main():
    print(f"NetRapier v{VERSION} (C) {AUTHOR}    {LINK}")
    app = QApplication(sys.argv)

    window = NetRapierWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
