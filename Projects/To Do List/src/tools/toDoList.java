package tools;

import java.util.HashMap;
import java.util.Set;

public class toDoList {
    private HashMap<String, String> tasksAndStatus = 
        new HashMap<String, String>();

    public toDoList(){

    }
    
    public toDoList(String task){
        tasksAndStatus.put(task, "incomplete");
    }

    public toDoList(String task, String status) {
        tasksAndStatus.put(task, status);
    }
    
    public void viewTasks() {
        Set<String> keys = tasksAndStatus.keySet();
        
        for (String key : keys){
            String keyStatus = tasksAndStatus.get(key);
            System.out.println("Task: "+key+", Status: "+keyStatus);
        }
        System.out.println("");
    }

    public void addNewTask(String newTask){
        tasksAndStatus.putIfAbsent(newTask, "incomplete");
    }
    
    public void addNewTask(String newTask, String status){
        tasksAndStatus.putIfAbsent(newTask, status);
    }

    public void changeStatus(String task, String newStatus){
        tasksAndStatus.replace(task, newStatus);
    }

    public void removeTask(String task){
        tasksAndStatus.remove(task);
    }

}