import tools.toDoList;

public class App {
    public static void main(String[] args) throws Exception {
        toDoList list = new toDoList();

        list.addNewTask("Go shopping");
        list.addNewTask("Check to do list", "In progress");
        list.addNewTask("Book train ticket");

        list.viewTasks();

        list.changeStatus("Check to do list", "complete");
        list.viewTasks();

        list.removeTask("Check to do list");
        list.viewTasks();
    }
}
