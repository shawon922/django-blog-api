var djblog = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        'appTitle': 'Django Blog',
        'posts': []
    },
    mounted: function() {
        //console.log('hi...');
        this.$http.get('http://127.0.0.1:8000/api/posts/').then(function(response) {
                this.posts = response.data.results;
                console.log(response.data);
            },
            function(response) {
                console.log(response);
            }
        ); 
    }
});


// var demo = new Vue({
//     el: '#app',
//     data: {
//         'apptitle': 'Django Vue.JS Job Board',
//         'jobs': []
//     },
//     methods: {
//         addJob: function () {
//             var newJob = {
//                 jobtitle: this.jobtitle.trim(),
//                 jobdescription: this.jobdescription.trim()
//             };

//             this.$http.post('http://127.0.0.1:8000/api/jobs/', newJob);
//         },
//         removeJob: function (index) {
//             this.$http.delete('http://127.0.0.1:8000/api/jobs/'.concat(this.jobs[index].id));
//             this.jobs.splice(index, 1);
//         }
//     },
//     ready: function()
//         {
//             this.$http.get('http://127.0.0.1:8000/api/jobs/').then(function (response) {
//                 this.jobs = response.data;
//             },
//             function (response) {
//                 console.log(response);
//             });
//         }
// });