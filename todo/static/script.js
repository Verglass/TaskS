$(document).ready(function() {

    function sort_tasklist() {
        $(".task").each(function( index ) {
    
            let task_id = $(this).attr('task_id');
            
            let current_task = index + 1;
    
            $.ajax({
                url: '/task/sort',
                type: 'POST',
                data: { pos: current_task, id: task_id }
            })
        });
    };

    function add_sortable() {
        $("#taskList").sortable({
            stop: sort_tasklist
        });
    };

    $(document).on('click', '.new-task-btn', function() {
        
        let user_id = $(this).attr('user_id');

        let description = $('#newInput'+user_id).val();

        $.ajax({
            url: '/task/create',
            type: 'POST',
            data: { desc: description, id: user_id },
            success: function(data) {
                $(taskList).replaceWith(data)
                sort_tasklist();
                $('#newInput'+user_id).val('')
                add_sortable();
            }
        });

    });

    $(document).on('click', '.delete-task-btn', function() {
        
        let task_id = $(this).attr('task_id');

        $.ajax({
            url : '/task/delete',
            type : 'POST',
            data : { id : task_id },
            success : function() {
                $('#taskSection'+task_id).remove();
            }
        });

    });

    $(document).on('blur', '.edit-task', function() {
        
        let task_id = $(this).attr('task_id');

        let description = $('#taskInput'+task_id).val();

        $.ajax({
            url : '/task/edit',
            type : 'POST',
            data : { desc : description, id : task_id }
        });

    });

    add_sortable();

});