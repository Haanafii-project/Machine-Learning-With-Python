import PySimpleGUI as sg

def create_window():
    """Creates the main application window with proper element imports."""
    layout = [
        [sg.Text('Masukkan Nama: '), sg.InputText()],
        [sg.Button('OK'), sg.Button('Batal')]
    ]

    return sg.Window('Contoh Aplikasi', layout)

def main():
    """Main loop for the application, handling events and displaying messages."""
    window = create_window()

    while True:
        event, values = window.read()
        if event in (None, 'Batal'):
            break
        if event == 'OK':
            sg.popup(f'Hello, {values[0]}!')

    window.close()

if __name__ == "__main__":
    main()