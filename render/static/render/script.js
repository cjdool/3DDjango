// common variables
var iBytesUploaded = 0;
var iBytesTotal = 0;
var iPreviousBytesLoaded = 0;
var iMaxFilesize = 1048576 * 200; // 200MB
var oTimer = 0;
var sResultFileSize = '';

function fileSelected() {

    // hide different warnings
    document.getElementById('error').style.display = 'none';
    document.getElementById('warnsize').style.display = 'none';

    // get selected file element
    var oFile = document.getElementById('zip_file').files[0];

    // filter for image files
    var rFilter = /^[^.]+.zip$/i;
    if (! rFilter.test(oFile.type)) {
        document.getElementById('error').style.display = 'block';
        return;
    }

    // little test for filesize
    if (oFile.size > iMaxFilesize) {
        document.getElementById('warnsize').style.display = 'block';
        return;
    }

}

function uploadFile() {
    var form = $('#FILE_FORM')[0];
    var formData = new FormData(form);
    formData.append("email", $("#email"));
    formData.append("file", $("#zip_file")[0].files[0]);

    $.ajax({
        url: '',
            processData: false,
            contentType: false,
            data: formData,
            type: 'POST',
            datatype: 'json',
            success: function(response){
                alert('Success')
                window.location.replace("{% url 'home' %}")
            },
            error: function(response){
                alert('Fail')
                window.location.replace("{% url 'service' %}")
            }
    });
}