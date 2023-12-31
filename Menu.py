import Data

def show_menu():
    print("Witaj! Wybierz opcję");
    print("1. Nowa gra");
    print("2. Wczytaj");
    print("3. Utwórz");
    print("4. Opcje");
    print("5. Wyjście");

def create_menu():
    print("1. Utwórz wroga");
    print("2. Utwórz nową lokację");
    print("3. Utwórz przedmiot");
    print ("4. Dodaj sklep");
    print ("5. Stwórz nagrodę");
    print ("6. Dodaj Wydarzenie");
    print("7. Dodaj pułapke");

def main():
    while True:
        show_menu();
        choice = input("Wybierz opcję (1-5): ");

        if choice == '1':
            print("Wybrałeś opcję Nowa gra.");
            Data.newGame();
            break;
        elif choice == '2':
            Data.load();
            break;
        elif choice == '3':
                create_menu();
                sub_choice = input("Wybierz opcję (1-6) lub 'exit' aby wrócić do poprzedniego menu: ");

                if sub_choice == '1':
                    Data.AddEnemyToFile();
                elif sub_choice == '2':
                    Data.AddLocationToFile();
                elif sub_choice == '3':
                    Data.AddItemToFile();
                elif sub_choice == '4':
                    Data.AddShopToFile();
                elif sub_choice == '5':
                    Data.AddRedvardToFile();
                elif sub_choice == '6':
                    Data.AddEeventToFile();
                elif sub_choice == '7':
                    Data.AddTrapToFile();
                elif sub_choice.lower() == 'exit':
                    break;
                else:
                    print("Nieprawidłowy wybór. Wprowadź liczbę od 1 do 6");
        elif choice == '4':
            print("Opcje");
        elif choice == '5':
            print("Wychodzę z programu.");
            break;
        else:
            print("Nieprawidłowy wybór. Wprowadź liczbę od 1 do 5.");

if __name__ == "__main__":
    main();