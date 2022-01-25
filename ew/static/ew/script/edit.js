let verb = document.getElementById('id_wverb');

function Check(){
    let pt = document.getElementById('tr_pt');
    let pp = document.getElementById('tr_pp');
    let prp = document.getElementById('tr_prp');
    if (verb.checked){
        pt.style.display = "table-row";
        pp.style.display = "table-row";
        prp.style.display = "table-row";

    }else{
        pt.style.display = "none";
        pp.style.display = "none";
        prp.style.display = "none";
}};


Check();
verb.addEventListener('change', Check); 