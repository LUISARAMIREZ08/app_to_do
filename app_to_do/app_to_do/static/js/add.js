$(document).ready(function() {
    $('.task-checkbox').on('change', function() {
        var taskId = $(this).data('task-id');
        var completed = $(this).prop('checked');
        $.ajax({
            url: '/update_task_status/',
            method: 'POST',
            data: {
                task_id: taskId,
                completed: completed ? 'true' : 'false',
                csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val()
            },
            success: function(response) {
                console.log('Estado de tarea actualizado correctamente');
            },
            error: function(xhr, status, error) {
                console.error('Error al actualizar el estado de la tarea:', error);
            }
        });
    });
});
