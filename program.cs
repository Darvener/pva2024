using System;
using System.Collections.Generic;

class Program
{
    static void Main(string[] args)
    {
        TodoList todoList = new TodoList("Todo List");
        TodoItem item1 = new TodoItem("Nakoupit potraviny", DateTime.Today.AddDays(0), "Mléko, chléb, vejce");
        todoList.AddTodoItem(item1);
        TodoItem item2 = new TodoItem("Napsat zprávu", DateTime.Today.AddDays(2), "Odpovědět na e-maily");
        todoList.AddTodoItem(item2);

        todoList.DisplayAllTodoItems();
        //todoList.AddTodoItem(itemNUMBER); - přidání todo do seznamu
        //todoList.RemoveTodoItem(itemNUMBER); - odstranění todo
        //todoList.CompleteTodoItem(itemNUMBER); - označení todo jako completed
    }
}

public class TodoItem
{
    public string Title { get; set; }
    public DateTime Due { get; set; }
    public DateTime CreatedAt { get; set; }
    public string Description { get; set; }
    public bool IsCompleted { get; set; }
    public TodoItem(string title, DateTime due, string description = "")
    {
        Title = title;
        Due = due;
        CreatedAt = DateTime.Now;
        Description = description;
        IsCompleted = false;
    }
}

public class TodoList
{
    public string Title { get; set; }
    private List<TodoItem> items;
    public TodoList(string title)
    {
        Title = title;
        items = new List<TodoItem>();
    }
        public void DisplayAllTodoItems()
    {
        Console.WriteLine($"Todo list: {Title}");
        foreach (var item in items)
        {
            Console.WriteLine($"Title: {item.Title}, Due: {item.Due}, Description: {item.Description}, Completed: {item.IsCompleted}");
        }
    }
    public void AddTodoItem(TodoItem item)
    {
        items.Add(item);
    }
    public void RemoveTodoItem(TodoItem item)
    {
        items.Remove(item);
    }
    public void CompleteTodoItem(TodoItem item)
    {
        item.IsCompleted = true;
    }
}