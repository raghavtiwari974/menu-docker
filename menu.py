import os

while True:
    print("""
Welcome to Docker Menu
-----------------------
1. Run a new Docker container
2. Stop a running container
3. Remove a container
4. Start a stopped container
5. List Docker images
6. List all containers
7. Exit
""")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name of container: ")
        image = input("Enter the name of image: ")
        os.system(f"docker run -dit --name {name} {image}")

    elif choice == "2":
        name = input("Enter name of container: ")
        os.system(f"docker stop {name}")

    elif choice == "3":
        name = input("Enter name of container: ")
        os.system(f"docker rm -f {name}")

    elif choice == "4":
        name = input("Enter name of container: ")
        os.system(f"docker start {name}")

    elif choice == "5":
        os.system("docker images")

    elif choice == "6":
        os.system("docker ps -a")

    elif choice == "7":
         print("Exiting Docker Menu. Goodbye!")
         break

    else:
        print("Enter a proper option:")
