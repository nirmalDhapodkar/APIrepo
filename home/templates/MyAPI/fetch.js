document.addEventListener('DOMContentLoaded', function() {
    // Define a function to fetch data from the backend
    function fetchData() {
        fetch('/fetch/')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                // Handle successful response
                console.log(data);
                // Do something with the predictions
            })
            .catch(error => {
                // Handle error
                console.error('Error fetching predictions:', error);
            });
    }

    // Call fetchData initially
    fetchData();

    // Set up interval to fetch data every 5 minutes (300,000 milliseconds)
    setInterval(fetchData, 300000); // 300,000 ms = 5 min
});