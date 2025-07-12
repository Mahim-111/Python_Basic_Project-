"""
Personal Task Manager

A command-line task management application that allows users to:
- Add new tasks with descriptions and status
- View all existing tasks
- Update task descriptions
- Mark tasks as complete
- Delete completed tasks
- Clean up duplicate tasks

Tasks are stored in a text file (tasks.txt) with the format:
ID | Description | Status

Author: Md Mahim Babu
Date: July 12, 2025
Version: 1.0
"""

import os

def add_task():
    """
    Add a new task to the tasks file.
    
    This function:
    1. Determines the next available task ID by finding the highest existing ID
    2. Prompts user for task description and status
    3. Appends the new task to the tasks.txt file
    
    The task ID is automatically generated to avoid conflicts, even after 
    tasks have been deleted.
    
    Raises:
        FileNotFoundError: Handled gracefully - starts with ID 1 if file doesn't exist
    """
    with open('tasks.txt', 'a') as file:
        try:
            with open('tasks.txt', 'r') as read_file:
                existing_tasks = read_file.readlines()
                if existing_tasks:
                    # Find the highest existing task ID to avoid conflicts
                    max_id = 0
                    for task in existing_tasks:
                        if task.strip():
                            try:
                                current_id = int(task.split('|')[0].strip())
                                max_id = max(max_id, current_id)
                            except (ValueError, IndexError):
                                # Skip malformed lines
                                continue
                    task_id = max_id + 1
                else:
                    task_id = 1
        except FileNotFoundError:
            # File doesn't exist yet, start with ID 1
            task_id = 1
        
        # Get user input for task details
        description = input("Enter task description: ")
        status = input("Enter task status (pending/completed): ")
        
        # Write task to file in format: ID | Description | Status
        file.write(f"{task_id} | {description} | {status}\n")
        print(f"Task added successfully with ID {task_id}.")

def view_tasks():
    """
    Display all tasks from the tasks file.
    
    Reads the tasks.txt file and displays each task in a formatted way.
    If no tasks exist or the file is not found, appropriate messages are shown.
    
    Raises:
        FileNotFoundError: Handled gracefully - shows message to add tasks first
    """
    try:
        with open('tasks.txt', 'r') as file:
            tasks = file.readlines()
            if tasks:
                print("Tasks:")
                for task in tasks:
                    print(task.strip())
            else:
                print("No tasks available.")
    except FileNotFoundError:
        print("No tasks file found. Please add a task first.")


def update_task_description():
    """
    Update the description of an existing task.
    
    This function:
    1. Prompts user for task ID to update
    2. Prompts for new description
    3. Updates only the matching task while preserving others
    4. Provides feedback on whether the task was found and updated
    
    The function handles tasks with varying spaces around pipe separators
    by using proper string parsing instead of simple prefix matching.
    
    Raises:
        FileNotFoundError: Handled gracefully - shows message if no tasks exist
    """
    try:
        task_id = input("Enter task ID to update: ")
        updated_description = input("Enter the new task description: ")

        # Read all existing tasks
        with open ("tasks.txt", 'r') as file:
            tasks = file.readlines()

        task_found = False
        # Rewrite file with updated task
        with open ('tasks.txt', 'w') as file:
            for task in tasks:
                # Parse task components and check for matching ID
                task_parts = task.split("|")
                if len(task_parts) >= 3 and task_parts[0].strip() == task_id:
                    # Update description while preserving ID and status
                    task = f"{task_parts[0]} | {updated_description} | {task_parts[2]}"
                    task_found = True
                file.write(task)
        
        # Provide appropriate feedback
        if task_found:
            print("Task description updated.")
        else:
            print(f"Task with ID {task_id} not found.")
    except FileNotFoundError:
        print("No tasks available to update.")


def mark_task_complete():
    """
    Mark a pending task as completed.
    
    This function:
    1. Prompts user for task ID to mark as complete
    2. Searches for the task with matching ID and "pending" status
    3. Changes the status from "pending" to "completed"
    4. Provides feedback on whether the operation was successful
    
    Only tasks with "pending" status can be marked as complete.
    Tasks already marked as "completed" will not be changed.
    
    Raises:
        FileNotFoundError: Handled gracefully - shows message if no tasks exist
    """
    try:
        task_id = input("Enter task ID to mark as complete: ")
        
        # Read all existing tasks
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

        task_found = False
        # Rewrite file with updated task status
        with open("tasks.txt", 'w') as file:
            for task in tasks: 
                # Parse task components and check for matching ID with pending status
                task_parts = task.split("|")
                if len(task_parts) >= 3 and task_parts[0].strip() == task_id and "pending" in task:
                    # Change status from pending to completed
                    task = task.replace("pending", "completed")
                    task_found = True
                file.write(task)
        
        # Provide appropriate feedback
        if task_found:
            print("Task marked as complete.")
        else:
            print(f"Task with ID {task_id} not found or already completed.")
    except FileNotFoundError:
        print("No tasks available to update")

def delete_completed_tasks():
    """
    Delete all tasks marked as completed.
    
    This function removes all tasks that contain "completed" in their status,
    keeping only pending tasks. This helps clean up the task list by removing
    finished work.
    
    The function rewrites the entire tasks file with only the remaining tasks.
    
    Raises:
        FileNotFoundError: Handled gracefully - shows message if no tasks exist
    """
    try:
        # Read all existing tasks
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

        # Rewrite file with only non-completed tasks
        with open("tasks.txt", 'w') as file:
            for task in tasks:
                # Keep only tasks that don't contain "completed"
                if "completed" not in task:
                    file.write(task)
        print("All completed tasks deleted.")
    except FileNotFoundError:
        print("No tasks available to delete.")

def clean_tasks_file():
    """
    Clean up the tasks file by removing duplicates and fixing formatting.
    
    This utility function:
    1. Reads all tasks from the file
    2. Removes duplicate entries while preserving order
    3. Strips whitespace and ensures consistent formatting
    4. Rewrites the file with cleaned data
    
    This function is automatically called when the program starts to ensure
    data integrity, and can also be manually triggered by the user.
    
    Args:
        None
    
    Returns:
        None
    
    Raises:
        FileNotFoundError: Handled gracefully - no action needed if file doesn't exist
    """
    try:
        # Read all existing tasks
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        
        # Remove duplicates while preserving order
        seen_tasks = set()
        unique_tasks = []
        
        for task in tasks:
            task = task.strip()  # Remove leading/trailing whitespace
            # Add task if it's not empty and not already seen
            if task and task not in seen_tasks:
                seen_tasks.add(task)
                unique_tasks.append(task)
        
        # Rewrite the file with cleaned tasks
        with open("tasks.txt", "w") as file:
            for task in unique_tasks:
                file.write(task + "\n")
                
    except FileNotFoundError:
        # File doesn't exist yet, that's okay
        pass

def main():
    """
    Main function that runs the Task Manager application.
    
    This function:
    1. Cleans up any duplicate tasks when the program starts
    2. Displays the main menu with available options
    3. Handles user input and calls appropriate functions
    4. Continues running until user chooses to exit
    
    The menu provides the following options:
    1. Add New Task
    2. View All Tasks
    3. Update Task Description
    4. Mark Task as Complete
    5. Delete Completed Tasks
    6. Clean Tasks File
    7. Exit
    
    Args:
        None
    
    Returns:
        None
    """
    # Clean up any duplicate tasks when program starts
    clean_tasks_file()
    
    # Main application loop
    while True:
        # Display menu options
        print("\nPersonal Task Manager:")
        print("--------------------")
        print("1. Add New Task")
        print("2. View All Tasks")
        print("3. Update Task Description")
        print("4. Mark Task as Complete")
        print("5. Delete Completed Tasks")
        print("6. Clean Tasks File")
        print("7. Exit")

        # Get user choice
        choice = input("Enter your choice: ")

        # Handle user selection
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            update_task_description()
        elif choice == '4':
            mark_task_complete()
        elif choice == '5':
            delete_completed_tasks()
        elif choice == '6':
            clean_tasks_file()
            print("Tasks file cleaned.")
        elif choice == '7':
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    """
    Program entry point.
    
    This ensures that the main() function is only called when the script
    is run directly, not when it's imported as a module.
    """
    main()