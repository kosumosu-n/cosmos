let spell = document.getElementById('id_spell');
spell.addEventListener('input', ()=>{
    spell.style.height = '26px';
    let scrollHeight = spell.scrollHeight;
    spell.style.height = scrollHeight -4 + 'px';
    console.log("success")
});


let ts = document.getElementById('id_ts');
ts.addEventListener('input', ()=>{
    ts.style.height = '26px';
    let scrollHeight = ts.scrollHeight;
    ts.style.height = scrollHeight -4 + 'px';
});


let pt = document.getElementById('id_pt');
pt.addEventListener('input', ()=>{
    pt.style.height = '26px';
    let scrollHeight = pt.scrollHeight;
    pt.style.height = scrollHeight -4 + 'px';
});


let pp = document.getElementById('id_pp');
pp.addEventListener('input', ()=>{
    pp.style.height = '26px';
    let scrollHeight = pp.scrollHeight;
    pp.style.height = scrollHeight -4 + 'px';
});


let prp = document.getElementById('id_prp');
prp.addEventListener('input', ()=>{
    prp.style.height = '26px';
    let scrollHeight = prp.scrollHeight;
    prp.style.height = scrollHeight -4 + 'px';
});


let fields = document.getElementById('fields');
let main = document.getElementsByTagName("main")[0]
let sample = document.getElementsByClassName('sample');
let verb = document.getElementById('switch_input');
function WindowChange(){
    sample.item(0).style.display = "none";
    sample.item(1).style.display = "none";
    sample.item(2).style.display = "none";
    if (verb.checked == true){
        let nline = Math.floor(main.clientWidth / 251);
        if (nline != 1){
            document.getElementById("fields").style.width = 251 * nline + 'px';
        }
        if (nline == 2){
            sample.item(0).style.display = "block";
            sample.item(1).style.display = "block";
            sample.item(2).style.display = "block";
        }else if (nline== 3){
            sample.item(0).style.display = "none";
            sample.item(1).style.display = "block";
            sample.item(2).style.display = "none";
        }else if (nline== 4){
            sample.item(0).style.display = "none";
            sample.item(1).style.display = "none";
            sample.item(2).style.display = "block";
        }
    }
};


let divpt = document.getElementById('pt');
let divpp = document.getElementById('pp');
let divprp = document.getElementById('prp');

function Check(){
    WindowChange()
    if (verb.checked){
        fields.style.justifyContent = "flex-start";
        divpt.style.display = "block";
        divpp.style.display = "block";
        divprp.style.display = "block";

    }else{
        fields.style.justifyContent = "center";
        divpt.style.display = "none";
        divpp.style.display = "none";
        divprp.style.display = "none";
}};

let spelltext = document.getElementById('id_spell')
function spellchange(){
    sample.item(0).innerHTML= spelltext.value.split('\n').join('<br>');
    sample.item(1).innerHTML= spelltext.value.split('\n').join('<br>');
    sample.item(2).innerHTML= spelltext.value.split('\n').join('<br>');

}

WindowChange();
verb.addEventListener('change', Check);
window.addEventListener('resize', WindowChange);
spelltext.addEventListener('input', spellchange);