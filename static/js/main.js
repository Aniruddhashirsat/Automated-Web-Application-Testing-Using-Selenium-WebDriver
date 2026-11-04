// STAQA Selenium Testing - Client JavaScript
document.addEventListener('DOMContentLoaded', function () {
    // Optional auto-dismiss alerts after 7 seconds
    const alerts = document.querySelectorAll('.alert-dismissible');
    alerts.forEach(function (alert) {
        setTimeout(function () {
            const bsAlert = bootstrap.Alert.getOrCreateInstance(alert);
            if (bsAlert) {
                bsAlert.close();
            }
        }, 8000);
    });
});
