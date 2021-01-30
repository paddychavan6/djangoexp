var vidname=""

function nexta(){
    document.getElementById('v1').style.display ="none";
    document.getElementById('v2').style.display="block";
    vidname=document.getElementById('vidname').value
}
function setvoterid(){
    document.getElementById('setvid').value=vidname
}
function backa(){

}
function setcam(){
    Webcam.set({
        width: 220,
        height: 190,
        image_format: 'jpeg',
        jpeg_quality: 100
    });
    Webcam.attach('#camera');
    document.getElementById('snapbutton').style.display = 'block';
    //document.getElementById('vid').value=voterid;
}

    // TAKE A SNAPSHOT.
    takeSnapShot = function () {
        vid=document.getElementById('vid').value;
            if(vid!=""){
                Webcam.snap(function (data_uri) {
                    voterid=document.getElementById('vid').value
                    downloadImage(voterid, data_uri);
                });
                document.getElementById('nexta').style.display = 'block';
                }
            else{
                alert("Please enter VoterID");
            }
            }

    // DOWNLOAD THE IMAGE.
    downloadImage = function (name, datauri) {
        name = voterid;
        var a = document.createElement('a');
        a.setAttribute('download', name + '.png');
        a.setAttribute('href', datauri);
        a.click();
    }