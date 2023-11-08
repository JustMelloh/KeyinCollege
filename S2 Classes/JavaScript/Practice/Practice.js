/* Javascript program that creates, deletes and allows tasks to be deleted.
 */

// Task list data structure
const tasks = [];

// Function to add a new task
function addTask() {
  const taskInput = document.getElementById("taskInput");
  const taskDescription = taskInput.value;
  if (taskDescription) {
    tasks.push({ description: taskDescription, completed: false });
    taskInput.value = "";
    displayTasks();
  }
}

// Function to display tasks
function displayTasks() {
  const taskList = document.getElementById("taskList");
  taskList.innerHTML = "";

  const filterValue = document.getElementById("filter").value;
  const filteredTasks =
    filterValue === "all"
      ? tasks
      : tasks.filter(
          (task) =>
            (filterValue === "completed" && task.completed) ||
            (filterValue === "pending" && !task.completed)
        );

  for (let i = 0; i < filteredTasks.length; i++) {
    const task = filteredTasks[i];
    const taskItem = document.createElement("li");

    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";
    checkbox.checked = task.completed;
    checkbox.onclick = () => toggleCompletion(i);
    taskItem.appendChild(checkbox);

    const description = document.createElement("span");
    description.innerText = task.description;
    taskItem.appendChild(description);

    const deleteButton = document.createElement("button");
    deleteButton.innerHTML = '<i class="fas fa-trash"></i>';
    deleteButton.onclick = () => deleteTask(i);
    taskItem.appendChild(deleteButton);

    taskList.appendChild(taskItem);
  }
}

// Function to toggle task completion
function toggleCompletion(index) {
  tasks[index].completed = !tasks[index].completed;
  displayTasks();
}

// Function to delete a task
function deleteTask(index) {
  tasks.splice(index, 1);
  displayTasks();
}

// Function to filter tasks
function filterTasks() {
  displayTasks();
}

// Initial display
displayTasks();
