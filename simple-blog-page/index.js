function this_year(){
    /** This function retrieve current year we are */

    var this_year = new Date();
    document.getElementById("this_year").innerHTML = this_year.getFullYear();
}
