// ------------------- Indicator -----------------------------
function Indicator (id, label) {
    this.id = id
    this.label = label
    this.yc = 0
    this.xc = 0
    this.h = 0
    this.w = 0
    this.ctx = null

    this.openMenu  = closeMenu
    this.closeMenu = closeMenu
    this.configure = configure
}

function openMenu(){
    ge("menu_"+this.id).style.display = "block"
}

function closeMenu(){
    ge("menu_"+this.id).style.display = "none"
}

function configure(){
    this.closeMenu()
    window.open('/indicator_config/'+this.id, '_blank')
}
// -----------------------------------------------------------

// ------------------- Tank -----------------------------
function Tank (id, label, min_level, capacity) {
    this.min_level = min_level
    this.capacity = capacity
    
    this.base = Indicator
    this.base(id, label)

    this.updateValue = updateTankValue
    this.openMenu  = openMenu
}
Tank.prototype = new Indicator

function updateTankValue(value) {
    if (value >= 0 && value <= 100) {
        let texto = value * this.capacity / 100 + " lts"
        ge("display_"+this.id).innerHTML = texto

        if (value > this.min_level) {
            this.ctx.fillStyle = "#0000FF"
        } else {
            this.ctx.fillStyle = "#FF0000"
        }

        this.ctx.clearRect(this.xc - this.w / 2 + 1, 0.2 * this.h + 1, 
            this.w - 2, this.h - 2)
        this.ctx.fillRect(this.xc - this.w / 2 + 1,
            (1 - value / 100) * (this.h - 2) + 0.2 * this.h + 1,
            this.w - 2, (value / 100) * (this.h - 2))
    } else {
        ge("display_"+this.id).innerHTML = "Valor incorrecto!!"
    }
}

// ------------------------------------------------------------------

// ------------------- Lower Tank -----------------------------
function LowerTank(id, label, min_level, capacity) {    
    this.drawTemplate = drawLowerTankTemplate
    
    this.base = Tank
    this.base(id, label, min_level, capacity)
}
LowerTank.prototype = new Tank;

function drawLowerTankTemplate() {
    let canvas = ge("canvas_"+this.id)
    if (canvas.getContext) {
        const xc = 0.5 * canvas.width
        const yc = 0.5 * canvas.height
        let w = 0.8 * canvas.width
        let h = 0.6 * w
        if (h > (0.8 * canvas.height)) {
            h = 0.8 * canvas.height
            w = h / 0.6
        }
        this.h = h
        this.w = w
        this.xc = xc
        this.yc = yc

        let ctx = canvas.getContext('2d')
        this.ctx = ctx
        ctx.beginPath()
        ctx.moveTo(xc - w / 2, 0.2 * h)
        ctx.lineTo(xc - w / 2, 1.2 * h)
        ctx.lineTo(xc + w / 2, 1.2 * h)
        ctx.lineTo(xc + w / 2, 0.2 * h)
        ctx.stroke()
    }
}

// ---------------------------------------------------------------

// ------------------- Upper Tank -----------------------------

function UpperTank(id, label, min_level, capacity) {
    this.drawTemplate = drawUpperTankTemplate
    
    this.base = Tank
    this.base(id, label, min_level, capacity)
}
UpperTank.prototype = new Tank

function drawUpperTankTemplate() {
    let canvas = ge("canvas_"+this.id)
    if (canvas.getContext) {
        const xc = 0.5 * canvas.width
        const yc = 0.5 * canvas.height
        let h = 0.8 * canvas.height
        let w = 0.7 * h
        if (w > (0.95 * canvas.width)) {
            w = 0.95 * canvas.width
            h = w / 0.7
        }
        this.h = h
        this.w = w
        this.xc = xc
        this.yc = yc

        let ctx = canvas.getContext('2d')
        this.ctx = ctx
        ctx.fillStyle = "#000000"
        ctx.strokeRect(xc - w / 2, 0.2 * h, w, h)
        ctx.fillRect(xc - w / 4, 0.1 * h, w / 2, 0.1 * h)
    }
}

// ---------------------------------------------------------------


// ------------------- Pump -----------------------------
function Pump (id, label) {
    this.state = 0
    this.animationStage = 0
        
    this.base = Indicator
    this.base(id, label)

    this.updateValue = updatePumpValue
    this.drawTemplate = drawPumpTemplate
    this.animate = animatePump
    this.openMenu  = openMenu
}
Pump.prototype = new Indicator


function updatePumpValue(value) {
    this.state = value
    this.animate()
}

function animatePump() {
    const x0 = this.xc - 0.32 * this.w
    const w0 = 3 * this.w / 40
    if (this.state == 1) {
        if (ge("display_"+this.id).innerHTML = "Apagada") {
            ge("display_"+this.id).innerHTML = "Encendida"
        }
        this.ctx.fillStyle = "#0000FF"
        switch (this.animationStage) {
            case 0:
                this.ctx.clearRect(x0 - 1, this.yc
                    - 13 * this.h / 40, w0 + 1, 20 * this.h / 40)
                this.animationStage = 1
                break
            case 1:
                this.ctx.fillRect(x0, this.yc
                    - 3 * this.h / 40, w0, 10 * this.h / 40)
                this.animationStage = 2
                break
            case 2:
                this.ctx.fillRect(x0, this.yc
                    - 13 * this.h / 40, w0, 10 * this.h / 40)
                this.animationStage = 0
                break
        }
    } else {
        if (ge("display_"+this.id).innerHTML = "Encendida") {
            ge("display_"+this.id).innerHTML = "Apagada"
        }
        this.ctx.clearRect(x0 - 1, this.yc
            - 13 * this.h / 40, w0 + 1, 20 * this.h / 40)
    }
}

function drawPumpTemplate() {
    let canvas = ge("canvas_"+this.id)
    if (canvas.getContext) {
        const xc = 0.5 * canvas.width
        const yc = 0.5 * canvas.height
        let w = 0.8 * canvas.width
        let h = w
        if (h > (0.8 * canvas.height)) {
            h = 0.8 * canvas.height
            w = h
        }
        this.h = h
        this.w = w
        this.xc = xc
        this.yc = yc
        const pxl = w / 48
        const x0 = xc - 0.5 * w
        const y0 = 0.2 * h

        let ctx = canvas.getContext('2d')
        this.ctx = ctx

        ctx.beginPath()
        ctx.translate(x0, y0)
        ctx.moveTo(5 * pxl, 0)
        ctx.lineTo(8 * pxl, 0)
        ctx.lineTo(8 * pxl, 14 * pxl)
        ctx.lineTo(5 * pxl, 15 * pxl)
        ctx.lineTo(5 * pxl, 30 * pxl)
        ctx.lineTo(8 * pxl, 31 * pxl)
        ctx.lineTo(13 * pxl, 31 * pxl)
        ctx.moveTo(16 * pxl, 0)
        ctx.lineTo(13 * pxl, 0)
        ctx.lineTo(13 * pxl, 0)
        ctx.lineTo(13 * pxl, 34 * pxl)
        ctx.lineTo(16 * pxl, 34 * pxl)
        ctx.lineTo(21 * pxl, 28 * pxl)
        ctx.lineTo(24 * pxl, 28 * pxl)
        ctx.lineTo(25 * pxl, 32 * pxl)
        ctx.lineTo(46 * pxl, 32 * pxl)
        ctx.lineTo(47 * pxl, 31 * pxl)
        ctx.lineTo(47 * pxl, 15 * pxl)
        ctx.lineTo(46 * pxl, 14 * pxl)
        ctx.lineTo(25 * pxl, 14 * pxl)
        ctx.lineTo(24 * pxl, 18 * pxl)
        ctx.lineTo(21 * pxl, 18 * pxl)
        ctx.lineTo(16 * pxl, 12 * pxl)
        ctx.lineTo(13 * pxl, 12 * pxl)
        ctx.moveTo(29 * pxl, 14 * pxl)
        ctx.lineTo(29 * pxl, 28 * pxl)
        ctx.moveTo(32 * pxl, 27 * pxl)
        ctx.lineTo(41 * pxl, 27 * pxl)
        ctx.moveTo(32 * pxl, 23 * pxl)
        ctx.lineTo(41 * pxl, 23 * pxl)
        ctx.moveTo(32 * pxl, 19 * pxl)
        ctx.lineTo(41 * pxl, 19 * pxl)
        ctx.moveTo(43 * pxl, 10 * pxl)
        ctx.lineTo(43 * pxl, 8 * pxl)
        ctx.lineTo(31 * pxl, 8 * pxl)
        ctx.lineTo(29 * pxl, 10 * pxl)
        ctx.moveTo(30 * pxl, 35 * pxl)
        ctx.lineTo(26 * pxl, 38 * pxl)
        ctx.lineTo(24 * pxl, 38 * pxl)
        ctx.lineTo(24 * pxl, 40 * pxl)
        ctx.lineTo(46 * pxl, 40 * pxl)
        ctx.lineTo(46 * pxl, 38 * pxl)
        ctx.lineTo(44 * pxl, 38 * pxl)
        ctx.lineTo(40 * pxl, 35 * pxl)
        ctx.strokeRect(0, 20 * pxl, 5 * pxl, 6 * pxl)
        ctx.stroke()
        ctx.translate(-x0, -y0)
    }
}

// ---------------------------------------------------------------

// ------------------- Light -----------------------------
function Light (id, label) {
    this.state = 0
    
    this.base = Indicator
    this.base(id, label)
    
    this.updateValue = updateLightValue
    this.drawTemplate = drawLightTemplate
    this.openMenu  = openMenu
}
Light.prototype = new Indicator

function updateLightValue(value) {
    const pxl = this.w / 48
    ctx = this.ctx
    xc = this.xc
    yc = this.yc
    if (value) {
        this.state = 1
        ge("display_"+this.id).innerHTML = "Encendida"
        ctx.fillStyle = "#fafd08"
        ctx.beginPath()
        ctx.translate(xc, yc - 5 * pxl)
        ctx.arc(0, 0, 12 * pxl, 3 * Math.PI / 4, Math.PI / 4)
        ctx.lineTo(6 * pxl, 15.5 * pxl)
        ctx.lineTo(-6 * pxl, 15.5 * pxl)
        ctx.closePath()
        ctx.fill()
        for (let i = 0; i < 5; i++) {
            ctx.fillRect(14 * pxl, -pxl, 4 * pxl, 2 * pxl)
            ctx.rotate(- Math.PI / 4)
        }
        ctx.fillStyle = "#000000"
        ctx.rotate(5 * Math.PI / 4)
        ctx.translate(-xc, -yc + 5 * pxl)
    } else {
        this.state = 0
        ge("display_"+this.id).innerHTML = "Apagada"
        ctx.clearRect(0, 0, 2 * xc, 2 * yc)
        this.drawTemplate()
    }

}

function drawLightTemplate() {
    let canvas = ge("canvas_"+this.id)
    if (canvas.getContext) {
        const xc = 0.5 * canvas.width
        const yc = 0.5 * canvas.height
        let w = 0.8 * canvas.width
        let h = w
        if (h > (0.8 * canvas.height)) {
            h = 0.8 * canvas.height
            w = h
        }
        this.h = h
        this.w = w
        this.xc = xc
        this.yc = yc
        const pxl = w / 48

        let ctx = canvas.getContext('2d')
        this.ctx = ctx

        ctx.beginPath()
        ctx.translate(xc, yc - 5 * pxl)
        ctx.arc(0, 0, 12 * pxl, 3 * Math.PI / 4, Math.PI / 4)
        ctx.lineTo(6 * pxl, 15.5 * pxl)
        ctx.lineTo(-6 * pxl, 15.5 * pxl)
        ctx.closePath()
        ctx.stroke()
        ctx.beginPath()
        ctx.fillRect(-5 * pxl, 17 * pxl, 10 * pxl, 2 * pxl)
        ctx.fillRect(-5 * pxl, 20 * pxl, 10 * pxl, 2 * pxl)
        ctx.beginPath()
        ctx.arc(0, 18.4 * pxl, 7 * pxl, Math.PI / 4, 3 * Math.PI / 4)
        ctx.fill()
        ctx.translate(-xc, -yc + 5 * pxl)
    }
}

// ----------------------------------------------------------------------

// ------------------- Door -----------------------------
function Door(id, label) {
    this.state = 0
    
    this.updateValue = updateDoorValue
    this.drawTemplate = drawDoorTemplate
    
    this.base = Indicator
    this.base(id, label)
}
Door.prototype = new Indicator

function drawDoorTemplate() {
    let canvas = ge("canvas_"+this.id)
    if (canvas.getContext) {
        const xc = 0.5 * canvas.width
        const yc = 0.5 * canvas.height
        let w = 0.8 * canvas.width
        let h = w
        if (h > (0.8 * canvas.height)) {
            h = 0.8 * canvas.height
            w = h
        }
        this.h = h
        this.w = w
        this.xc = xc
        this.yc = yc
        const pxl = w / 100

        let ctx = canvas.getContext('2d')
        this.ctx = ctx
        ctx.lineWidth = 2
        ctx.translate(xc / 2, yc / 4)
        if (this.state) {
            ctx.beginPath()
            ctx.moveTo(78 * pxl, 86 * pxl)
            ctx.lineTo(87 * pxl, 86 * pxl)
            ctx.lineTo(87 * pxl, 11 * pxl)
            ctx.lineTo(64 * pxl, 11 * pxl)
            ctx.lineTo(78 * pxl, 18 * pxl)
            ctx.lineTo(78 * pxl, 86 * pxl)
            ctx.lineTo(49 * pxl, 95 * pxl)
            ctx.lineTo(49 * pxl, 5 * pxl)
            ctx.lineTo(64 * pxl, 11 * pxl)
            ctx.moveTo(49 * pxl, 18 * pxl)
            ctx.lineTo(42 * pxl, 18 * pxl)
            ctx.lineTo(42 * pxl, 86 * pxl)
            ctx.lineTo(34 * pxl, 86 * pxl)
            ctx.lineTo(34 * pxl, 40 * pxl)
            ctx.moveTo(34 * pxl, 26 * pxl)
            ctx.lineTo(34 * pxl, 11 * pxl)
            ctx.lineTo(49 * pxl, 11 * pxl)

            ctx.moveTo(56 * pxl, 47 * pxl)
            ctx.lineTo(56 * pxl, 61 * pxl)
        } else {
            ctx.strokeRect(34 * pxl, 11 * pxl, 53 * pxl, 75 * pxl)
            ctx.strokeRect(42 * pxl, 18 * pxl, 36 * pxl, 68 * pxl)
            ctx.clearRect(30 * pxl, 25 * pxl, 5 * pxl, 13 * pxl)
            ctx.moveTo(49 * pxl, 47 * pxl)
            ctx.lineTo(49 * pxl, 57 * pxl)
        }
        ctx.moveTo(37 * pxl, 29 * pxl)
        ctx.lineTo(37 * pxl, 36 * pxl)
        ctx.moveTo(31 * pxl, 29 * pxl)
        ctx.lineTo(31 * pxl, 36 * pxl)
        ctx.stroke()
        ctx.beginPath()
        ctx.arc(34 * pxl, 29 * pxl, 3 * pxl, Math.PI, 2 * Math.PI)
        ctx.arc(34 * pxl, 36 * pxl, 3 * pxl, 0, Math.PI)
        ctx.stroke()
        ctx.beginPath()
        ctx.moveTo(25 * pxl, 49 * pxl)
        ctx.lineTo(18 * pxl, 56 * pxl)
        ctx.moveTo(23 * pxl, 33 * pxl)
        ctx.lineTo(13 * pxl, 33 * pxl)
        ctx.moveTo(25 * pxl, 17 * pxl)
        ctx.lineTo(19 * pxl, 10 * pxl)
        ctx.stroke()

        ctx.translate(-xc / 2, -yc / 4)
    }
}

function updateDoorValue(value, door) {
    switch (value) {
        case 0:
            ge("display_"+this.id).innerHTML = "Cerrada"
            break
        case 1:
            ge("display_"+this.id).innerHTML = "Abierta"
            break
        default:
            ge("display_"+this.id).innerHTML = "Error"
            break
    }
    if (value != this.state) {
        this.state = value
        ctx = this.ctx
        w = this.w
        xc = this.xc
        yc = this.yc
        pxl = w / 100
        ctx.clearRect(xc / 3, yc / 5, 150 * pxl, 110 * pxl)
        switch (value) {
            case 0:
                this.drawTemplate()
                break
            case 1:
                this.drawTemplate()
                break
            default:
                this.drawTemplate()
                ctx.strokeStyle = "#ff0000"
                ctx.strokeRect(xc / 2, yc / 4, xc, 1.6 * yc)
                ctx.strokeStyle = "#000000"
                break
        }
    }
}

// --------------------------------------------------------------------

// ----------------------- Pir -----------------------------
function Pir(id, label, has_luminosity) {
    this.state = 0
    
    this.updateValue = updateMovementValue
    this.drawTemplate = drawMovementTemplate    
    
    this.base = Indicator
    this.base(id, label)
}
Pir.prototype = new Indicator

function drawMovementTemplate() {
    let canvas = ge("canvas_"+this.id)
    if (canvas.getContext) {
        const xc = 0.5 * canvas.width
        const yc = 0.5 * canvas.height
        let w = 0.8 * canvas.width
        let h = w
        if (h > (0.8 * canvas.height)) {
            h = 0.8 * canvas.height
            w = h
        }
        this.h = h
        this.w = w
        this.xc = xc
        this.yc = yc
        const pxl = w / 48

        let ctx = canvas.getContext('2d')
        this.ctx = ctx
        ctx.translate(2 * w / 3, 0)

        // Movement Sensor
        ctx.beginPath()
        ctx.moveTo(30 * pxl, 50 * pxl)
        ctx.lineTo(30 * pxl, 42 * pxl)
        ctx.lineTo(37 * pxl, 37 * pxl)
        ctx.lineTo(34 * pxl, 26 * pxl)
        ctx.lineTo(41 * pxl, 26 * pxl)
        ctx.lineTo(45 * pxl, 27 * pxl)
        ctx.lineTo(49 * pxl, 31 * pxl)
        ctx.lineTo(48 * pxl, 33 * pxl)
        ctx.lineTo(44 * pxl, 29 * pxl)
        ctx.lineTo(41 * pxl, 28 * pxl)
        ctx.lineTo(42 * pxl, 38 * pxl)
        ctx.lineTo(34 * pxl, 43 * pxl)
        ctx.lineTo(32 * pxl, 49 * pxl)
        ctx.closePath()
        ctx.fill()

        ctx.beginPath()
        ctx.arc(35 * pxl, 21 * pxl, 3 * pxl, 0, 2 * Math.PI)
        ctx.fill()

        ctx.fillRect(29 * pxl, 31 * pxl, 6 * pxl, 2 * pxl)

        ctx.beginPath()
        ctx.moveTo(41 * pxl, 40 * pxl)
        ctx.lineTo(43 * pxl, 39 * pxl)
        ctx.lineTo(49 * pxl, 48 * pxl)
        ctx.lineTo(49 * pxl, 49 * pxl)
        ctx.lineTo(47 * pxl, 49 * pxl)
        ctx.closePath()
        ctx.fill()

        ctx.beginPath()
        ctx.arc(18 * pxl, 11 * pxl, 3 * pxl, 0, Math.PI)
        ctx.fill()

        ctx.lineWidth = 3
        for (let i = 0; i < 4; i++) {
            ctx.beginPath()
            ctx.arc(18 * pxl, 11 * pxl, (6 + 4 * i) * pxl, 
                Math.PI / 12, 7 * Math.PI / 12)
            ctx.stroke()
        }
        ctx.translate(-2 * w / 3, 0)
    }
}

function updateMovementValue(value) {
    ctx = this.ctx
    w = this.w
    pxl = w / 48
    if (!this.has_luminosity) {
        ctx.translate(2 * w / 3, 0)
    }
    if (value) {
        ge("display_"+this.id).innerHTML = "Activado"
        ctx.strokeStyle = "#ff0000"
        ctx.strokeRect(10 * pxl, 5 * pxl, 45 * pxl, 50 * pxl)
        ctx.strokeStyle = "#000000"
        if (!this.has_luminosity) {
            ctx.translate(-2 * w / 3, 0)
        }
    }
    else {
        ge("display_"+this.id).innerHTML = "Inactivo"
        ctx.clearRect(9 * pxl, 4 * pxl, 47 * pxl, 52 * pxl)
        if (!this.has_luminosity) {
            ctx.translate(-2 * w / 3, 0)
        }
        this.drawTemplate()
    }
}

// ---------------------------------------------------------------------

// ----------------------- Ldr -----------------------------
function Ldr(id, label) {
    this.luminosity = 0
    
    this.updateValue = updateLuminosityValue
    this.drawTemplate = drawLdrTemplate
    
    this.base = Indicator
    this.base(id, label)
}
Ldr.prototype = new Indicator

function drawLdrTemplate() {
    let canvas = ge("canvas_"+this.id)
    if (canvas.getContext) {
        const xc = 0.5 * canvas.width
        const yc = 0.5 * canvas.height
        let w = 0.8 * canvas.width
        let h = w
        if (h > (0.8 * canvas.height)) {
            h = 0.8 * canvas.height
            w = h
        }
        this.h = h
        this.w = w
        this.xc = xc
        this.yc = yc
        const pxl = w / 48

        let ctx = canvas.getContext('2d')
        this.ctx = ctx
        // Luminosity sensor
        ctx.beginPath()
        ctx.lineWidth = 4
        ctx.arc(60 * pxl, 20 * pxl, 6 * pxl, 0, 2 * Math.PI)
        ctx.stroke()

        ctx.beginPath()
        ctx.translate(60 * pxl, 20 * pxl)
        for (let i = 0; i < 8; i++) {
            ctx.fillRect(8 * pxl, -pxl, 4 * pxl, 2 * pxl)
            ctx.rotate(Math.PI / 4)
        }
        ctx.translate(-60 * pxl, -20 * pxl)
        this.updateValue(this.luminosity)

    }
}

function updateLuminosityValue(value) {
    if (value < 0) {
        value = 0
    }
    if (value > 100) {
        value = 100
    }
    this.luminosity = value
    ge("display_"+this.id).innerHTML = value+"%"
    value = Math.round(value / 10)
    ctx = this.ctx
    w = this.w
    pxl = w / 48
    ctx.beginPath()
    ctx.translate(41 * pxl, 45 * pxl)
    ctx.clearRect(-pxl, -pxl, 45 * pxl, 5 * pxl)
    for (let i = 0; i < 10; i++) {
        if (value > i) {
            ctx.fillStyle = "#000000"
        } else {
            ctx.fillStyle = "#ababab"
        }
        ctx.fillRect(i * 4 * pxl, 0, 2 * pxl, 3 * pxl)
    }
    ctx.fillStyle = "#000000"
    ctx.translate(-41 * pxl, -45 * pxl)
}

// ---------------------------------------------------------------------




