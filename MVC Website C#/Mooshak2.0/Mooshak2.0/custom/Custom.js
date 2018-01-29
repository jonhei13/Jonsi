

$(document).ready(function(){
    //$("#Assignments").click(function(){ 
        
    //});



    $(".dropdown").click(function () {
        $(".dropdown-content").slideToggle()
    });

    $(function () {
        $('input:file').change(function () {
            $('#UserNameInput').attr('disabled', 'true')
        });
    });
    
    
    
});

$('#SelectAllCheckbox').click(function () {
    if ($('#SelectAllCheckbox').is(':checked'))
        $('.SelectCheckbox').prop("checked", true);
});

$('#SelectAllCheckbox').click(function () {
    if (!$('#SelectAllCheckbox').is(':checked'))
        $('.SelectCheckbox').prop("checked", false);

});

$(document).ready(function () {
    $('input[type=datetime]').datepicker({
        dateFormat: "dd/M/yy",
        changeMonth: true,
        changeYear: true,
        yearRange: "-60:+0"
    });

});

