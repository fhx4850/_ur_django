if (document.getElementById('menu-btn')){
    document.getElementById('menu-btn').onclick = function(){
        let menu_panel = document.getElementById('menu-panel');
        menu_panel.classList.toggle('panel-hide');
        panel_bg(menu_panel);
    }
}

function panel_bg(hide_object, hide_class='panel-hide', opacity='0', z_index=100){
    if(document.getElementById('panel-bg')){
        document.getElementById('panel-bg').style.opacity = opacity;
        document.getElementById('panel-bg').style.zIndex = z_index;
        document.getElementById('panel-bg').classList.toggle('panel-hide');
        document.getElementById('panel-bg').onclick = function(){
            hide_object.classList.add(hide_class);
            document.getElementById('panel-bg').classList.add('panel-hide');
        }
    }
}

if(document.getElementsByClassName('pub-menu-btn')){
    let pub_menu_btns = document.getElementsByClassName('pub-menu-btn');
    for (let i = 0; i < pub_menu_btns.length; i++) {
        pub_menu_btns[i].onclick = function(){
            document.getElementsByClassName('pub-panel')[i].classList.remove('panel-menu-hide');
            panel_bg(document.getElementsByClassName('pub-panel')[i], 'panel-menu-hide');
        }
    }
}

if(document.getElementsByClassName('repost_btn')){
    let repost_btns = document.getElementsByClassName('repost_btn');
    for (let i = 0; i < repost_btns.length; i++) {
        repost_btns[i].onclick = function(){

            document.getElementById('repost_s_alert').classList.toggle('panel-hide');
            panel_bg(document.getElementById('repost_s_alert'), 'panel-hide' ,'0.3', '101');

        }        
    }
}

if(document.getElementById('main_page_alert_close')){
    document.getElementById('main_page_alert_close').onclick = function(){
        document.getElementsByClassName('main_page_alert_wrap')[0].classList.add('panel-hide');
        document.getElementById('panel-bg').classList.add('panel-hide');
    }
}

if(document.getElementsByClassName('pub-load-more')){
    let pub_load = document.getElementsByClassName('pub-load-more');
    for (let i = 0; i < pub_load.length; i++) {
        pub_load[i].onclick = function(){
            s_text = document.getElementsByClassName('s-text');
            s_text[i].classList.toggle('load-more');
            if(s_text[i].classList.contains('load-more')){
                pub_load[i].innerHTML = 'Load more';
            }
            else{
                pub_load[i].innerHTML = 'Hide';
            }
        }        
    }
}

if(document.getElementById('pub-img-view')){
    let pub_img = document.getElementsByClassName('pub_img');
    document.getElementById('pub-img-view').onclick = function(){
        document.getElementById('pub-img-view').classList.add('img-view-hide');
    }
    for (let i = 0; i < pub_img.length; i++) {
        pub_img[i].onclick = function(){
            document.getElementById('pub-img-view-img').src = pub_img[i].src;
            document.getElementById('pub-img-view').classList.remove('img-view-hide');
        }
    }
}

if(document.getElementById('pub-detail-menu-panel-bg')){
    document.getElementById('pub-detail-menu-panel-bg').onclick = function(){
        console.log('sdvsdv');

    }
}

if(document.getElementById('create-pub-btn')){
    document.getElementById('create-pub-btn').onclick = function(){
        document.getElementById('content').innerHTML += "{% include '' %}"
    }
}

if(document.getElementById('cp_close')){
    document.getElementById('cp_close').onclick = function(){
        document.getElementById('cp-wrap').classList.add('cp-hide');
        document.getElementById('panel-bg').classList.add('panel-hide');
    }
}

if(document.getElementById('cp-images')){
    document.getElementById('cp-images').onclick = function(){
        document.getElementById('cp_imgs_input').click();
    }
}

document.getElementById('cp_imgs_input').onchange = function(e){
    document.getElementById('cp-imgs').innerHTML = '';
    let rr = e.target.files;
    let img_count = 0
    for (let i = 0; i < rr.length; i++) {
        let url = URL.createObjectURL(rr[i]);
        if(i < 2){
            document.getElementById('cp-imgs').innerHTML += '<div class="cp-img">'+
            '<img src="' + url + '" alt=""></div>';
        }
        img_count ++;
    }
    document.getElementById('img-count').innerHTML = img_count;
}


if(document.getElementById('create-pub-btn')){
    document.getElementById('create-pub-btn').onclick = function(){
        document.getElementById('cp-wrap').classList.remove('cp-hide');
        document.getElementById('menu-panel').classList.add('panel-hide');


        let panel_bg = document.getElementById('panel-bg');
        panel_bg.style.opacity = '0.3';
        panel_bg.style.zIndex = '101';
        panel_bg.classList.remove('panel-hide');
        panel_bg.onclick = function(){
            document.getElementById('cp-wrap').classList.add('cp-hide');
            panel_bg.classList.add('panel-hide');
        }
    }
}

if(document.getElementById('show-detail-btn')){
    let sd_btn = document.getElementById('show-detail-btn');
    sd_btn.onclick = function(){
        let pd_info = document.getElementById('pd-info')
        pd_info.classList.toggle('pdi-hide');
        if(pd_info.classList.contains('pdi-hide')){
            sd_btn.innerHTML = 'Show detail information';
        }
        else{
            sd_btn.innerHTML = 'Hide detail information';
        }
    }
}

if(document.getElementById('copy-profile-url')){
    document.getElementById('copy-profile-url').onclick = function(){
        navigator.clipboard.writeText(window.location.href);
    }
}

if (document.getElementById('my-follows-btn')){
    document.getElementById('my-follows-btn').onclick = function(){
        document.getElementById('follows_panel').classList.remove('panel-hide');
        document.getElementById('menu-panel').classList.add('panel-hide');


        let panel_bg = document.getElementById('panel-bg');
        panel_bg.style.opacity = '0.3';
        panel_bg.style.zIndex = '101';
        panel_bg.classList.remove('panel-hide');
        panel_bg.onclick = function(){
            document.getElementById('follows_panel').classList.add('panel-hide');
            panel_bg.classList.add('panel-hide');
        }
    }
}

if(document.getElementById('my_follows_close')){
    document.getElementById('my_follows_close').onclick = function(){
        document.getElementById('panel-bg').classList.add('panel-hide');
        document.getElementById('follows_panel').classList.toggle('panel-hide');
    }
}