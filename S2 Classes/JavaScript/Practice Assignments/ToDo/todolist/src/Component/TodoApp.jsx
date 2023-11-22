// TodoApp.js
import React, { useState, useEffect } from "react";
import "../Styles/ToDoApp.css";

const TodoApp = () => {
  const [todos, setTodos] = useState([]);

  useEffect(() => {
    const fetchTodos = async () => {
      try {
        const response = await fetch(
          "https://jsonplaceholder.typicode.com/todos"
        );
        const todosData = await response.json();
        setTodos(todosData);
      } catch (error) {
        console.error("Error fetching todos:", error);
      }
    };

    fetchTodos();
  }, []);

  
  const limitedTodos = todos.slice(0, 5);

  return (
    <div className="todo-container">
      <h1>Todo List</h1>
      {limitedTodos.length > 0 ? (
        <ul className="todo-list">
          {limitedTodos.map((todo) => (
            <li key={todo.id} className="todo-item">
              <span>{todo.title}</span>
              <span>{todo.completed ? "Completed" : "Pending"}</span>
            </li>
          ))}
        </ul>
      ) : (
        <p>No todos found</p>
      )}
    </div>
  );
};

export default TodoApp;
