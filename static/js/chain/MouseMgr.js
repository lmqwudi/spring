MouseMgr = function (mouseCircle){
    this.mouseCircle = mouseCircle;
};

MouseMgr.prototype = {
    mouseDown: function (event){
        this.mouseCircle.state = EXPEND;
        _ExpendStart =true;
        g_counter = 10;
        g_MouseEventDispatch.end();
    },
    mouseMove: function(event){
        this.mouseCircle.x = event.clientX-8;
        this.mouseCircle.y = event.clientY-8;
    },
    mouseUp: function(event){}
    };
