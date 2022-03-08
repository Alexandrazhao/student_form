<template>
    <div class="tasks_container">
        
        <div class="tasks_content">
            <h1>Student Form</h1>
            <table class="tasks_list">
                <thead>
                    <th>First name</th>
                    <th>Last name</th>
                    <th>e_mail</th>
                    <th>Major</th>
                    <th>Check in time</th>
                    <tr v-for="task in tasks" :key="task.id">
                        <td>{{ task.first_name }}</td>
                        <td>{{ task.last_name }}</td>
                        <td>{{task.e_mail}}</td>
                        <td>{{task.major}}</td>
                        <td>{{ task.check_in_time }}</td>
                        <button @click="deleteTask(task)">Delete</button>
                    </tr>
                </thead>
            </table>
            
        </div>
        <div class="add_task">
            <form v-on:submit.prevent="submitForm">
                <div class="form-group">
                    <label for="first_name">First Name</label>
                    <input type="text" class="form-control" id="first_name" v-model="first_name">
                </div>
                 <div class="form-group">
                     <label for="last_name">Last Name</label>
                    <textarea class="form-control" id="last_name" v-model="last_name"></textarea>
                </div>
                <div class="form-group">
                     <label for="e_mail">E-mail</label>
                     <input class="form-control" v-model="e_mail" type="e_mail" id="e_mail" pattern="^[a-z0-9]+@[a-z0-9]+\.edu$" size="50" required>
                    <!--textarea class="form-control" id="e_mail" v-model="e_mail"></textarea-->
                </div>
                <div class = "form-group">
                    <label for = "major">Major</label>
                    <select class="form-control" name = "major" id="major" v-model="major">
                        <option value="Math">Math</option>
                        <option value="English">English</option>
                        <option value="Physics">Physics</option>
                        <option value="Chemistry">Chemistry</option>
                    </select>
                </div>
                <!--div class="form-group">
                     <label for="major">Major</label>
                    <textarea class="form-control" id="major" v-model="major"></textarea>
                </div-->
                <div class="form-group">
                    <button type="submit">New User</button>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
    export default {
        data(){
            return {
                tasks: [],
                first_name: '',
                last_name: '',
                e_mail:'',
                major:''
            }
        },
        methods: {
            async getData() {
                try {
                    // fetch tasks
                    const response = await this.$http.get('http://localhost:8000/api/tasks/');
                    // set the data returned as tasks
                    this.tasks = response.data; 
                    //const response = await
                } catch (error) {
                    // log the error
                    console.log(error);
                }
            },
            async submitForm(){
                try {
                    // Send a POST request to the API
                    const response = await this.$http.post('http://localhost:8000/api/tasks/', {
                        first_name: this.first_name,
                        last_name: this.last_name,
                        e_mail:this.e_mail,
                        major:this.major,
                    });
                    // Append the returned data to the tasks array
                    this.tasks.push(response.data);
                    // Reset the title and description field values.
                    this.first_name = '';
                    this.last_name = '';
                    this.e_mail = '';
                    this.major = '';
                } catch (error) {
                    // Log the error
                console.log(error);
                }
            },
            async deleteTask(task) {
                // Confirm if one wants to delete the task
                let confirmation = confirm("Do you want to delete this task?");
                if (confirmation) {
                    try {
                    // Send a request to delete the task
                    await this.$http.delete(`http://localhost:8000/api/tasks/${task.id}`);
                    // Refresh the tasks
                    this.getData();
                    } catch (error) {
                    // Log any error
                    console.log(error);
                        }
                }
            }
        },
        created() {
            // Fetch tasks on page load
            this.getData();
        }
    }
</script>