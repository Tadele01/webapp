function applicationform(){
    var na=document.forms["applyform"]["name"].value;
    var em=document.forms["applyform"]["email"].value;
    var pn=document.forms["applyform"]["phoneno"].value;
    var em=document.forms["applyform"]["resumelink"].value;
    var tl=document.forms["applyform"]["testmonial"].value;
    if(na=="" || em=="" || pn=="" || em=="" || tl=="" ){
        document.getElementById('aa').innerHTML='all fields are required';

        return false;

    }


    else{
        return true;
    }
}