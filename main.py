from system import Program


def main():
    system = Program()

    while True:
        print("1. Create Project")
        print("2. Create Contract")
        print("3. List Projects")
        print("4. List Contracts")
        print("5. Confirm Contract")
        print("6. Complete Contract")
        print("7. Add contract to project")
        print("8. Exit")
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                name = input("Enter project name: ")
                system.create_project(name)
            case '2':
                name = input("Enter contract name: ")
                system.create_contract(name)
            case '3':
                system.list_projects()
            case '4':
                system.list_contracts()
            case '5':
                contract_id = int(input("Enter contract ID to confirm: "))
                system.confirm_contract(contract_id)
            case '6':
                contract_id = int(input("Enter contract ID to complete: "))
                system.complete_contract(contract_id)
            case '7':
                contract_name = input("Enter contract name to add to project: ")
                project_id = int(input("Enter project ID to add contract to: "))
                system.add_contract_to_project(contract_name, project_id)
            case '8':
                system.close()
                print("Goodbye!")
                break
            case _:
                print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()