document.addEventListener('DOMContentLoaded', function () {
    const scrollFadeElements = document.querySelectorAll('.scroll-fade');

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('in-view');
            } else {
                entry.target.classList.remove('in-view');
            }
        });
    }, {
        threshold: 0.1
    });

    scrollFadeElements.forEach(element => {
        observer.observe(element);
    });

    // Add event listener to the form submit button
    document.getElementById('form').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent form from submitting normally

        const firstName = document.getElementById('fname').value;


        alert(`${firstName}, Your details received Successfully...We will contact you soon...`);

        // Uncomment the following line if you want to submit the form after displaying the alert
        this.submit();
    });

    // Add event listener to the exit button
    document.getElementById('ex').addEventListener('click', function() {
        document.getElementById('fname').value = '';
        document.getElementById('lname').value = '';
        document.getElementById('email').value = '';
        document.getElementById('phone').value = '';
        document.getElementById('address').value = '';
        document.getElementById('course').value = 'none';
    });
});


