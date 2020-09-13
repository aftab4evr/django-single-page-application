$(document).ready(function () {
    $(document).on("click", ".user_top_box ", function () {
        $(".user_top_box .dropdown-menu").toggleClass("show");
    });

    $(document).click(function (e) {
        if (!$(e.target).is(".head-drop-down, .head-drop-down *, .user_top_box, .user_top_box *")) {
            $(".user_top_box .dropdown-menu").removeClass('show');
        }
    });

});


function ValidateFileUpload(input, image) {
    var fuData = document.getElementById("image");
    var FileUploadPath = fuData.value;
    var Extension = FileUploadPath.substring(
        FileUploadPath.lastIndexOf('.') + 1).toLowerCase();
    if (Extension == "png" || Extension == "jpeg" || Extension == "jpg") {
        if (fuData.files[0].size > 3e+6) {
            alert("File size must be less than or equal to 3 MB.");
            fuData.value = '';
            fuData.src = '';
        } else {
            if (fuData.files && fuData.files[0]) {
                var reader = new FileReader();
                reader.onload = function (e) {
                    $('#' + image).attr('src', e.target.result);
                }
                reader.readAsDataURL(fuData.files[0]);
            }
        }
    }
    else {
        fuData.value = '';
        alert('Please choose PNG, JPG and JPEG.')
        // alert("Photo only allows file types of  PNG, JPG and JPEG  ");

    }
}