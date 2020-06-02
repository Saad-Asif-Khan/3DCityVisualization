// your code
var StatesFileCount = [];
var viewer;
var Alltiles = [];
var a = 0;
var b = 0;
var Pageloaded;
var Tilescount = 0;
var Urls = [];
var scene;
var singleStateTilesCount = -1;
function Onload() {
    Getdata();
}
function Getdata() {
    $.ajax({
        async: true,
        type: "GET",
        url: "./WebService.asmx/HelloWorld",
        data: {},
        contentType: "application/json; charset=utf-8",
        success: OnSuccess,
        error: OnError,
        failure: OnFailed

    });
    function OnSuccess(Result) {

        //Make the path list acending order
        Result.d = Result.d.reverse();

        //CesiumIon Token Defined
        Cesium.Ion.defaultAccessToken = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJkNWJhMTNjMS03NzU2LTRhNzctYmZmYy0yZDBiNjFkODE0MDAiLCJpZCI6OTEyMywic2NvcGVzIjpbImFzciIsImdjIl0sImlhdCI6MTU1MzUzMzk5OH0.H5d_3hj6nPPU6Vai6bMJmeDq5UsxVIcwrcEFlnzhxD8';

        //Code adapted from Cesium Sandcastle example "3D Tiles format"
        viewer = new Cesium.Viewer('cesiumContainer', {
            shadows: true

        });
        viewer.scene.globe.depthTestAgainstTerrain = true;
        scene = viewer.scene;

        //write the name of each state in an array to add it to the dropdown
        SetStateNames(Result.d);

        document.getElementById("HeightImage").style.visibility = "visible";

        //for (var i = 0; i < Result.d.length; i++) {
        //    var tileset = new Cesium.Cesium3DTileset({
        //        url: "./" + Result.d[i],
        //    });
        //    Tilescount += 1;
        //    var TileSetName = Result.d[i].toString();
        //    TileSetName = TileSetName.split("/");
        //    TileSetName = TileSetName[TileSetName.length - 4];

        //    var stylingAttribute = "citygml_measured_height";

        //    // adding center tile from the tileset against the state Name
        //    AddingCenterTileset(tileset, TileSetName);

        //    //document.getElementById("NoOfTilesLoaded").innerHTML = i + " No of Tiles loaded";

        //    scene.primitives.add(tileset);

        //    tileset.readyPromise.then(function (tileset) {

        //        var properties = tileset.properties;

        //        Alltiles.push({ Tileset: tileset });
        //        //Alltiles[i].Tileset = tileset;
        //        //var valuereq = tileset[0].properties;

        //        if (Cesium.defined(properties) && Cesium.defined(properties[stylingAttribute])) {
        //            tileset.style = new Cesium.Cesium3DTileStyle({
        //                color: {
        //                    conditions: [
        //                        ["${" + stylingAttribute + "} === null", "color('white')"],
        //                        ["${" + stylingAttribute + "} >= 16", "color('maroon')"],
        //                        ["${" + stylingAttribute + "} >= 12", "color('red')"],
        //                        ["${" + stylingAttribute + "} >= 8", "color('yellow')"],
        //                        ["${" + stylingAttribute + "} >= 5", "color('lightgreen')"],
        //                        ["${" + stylingAttribute + "} >= 0", "color('blue')"],
        //                        ["true", "color('gray')"]
        //                    ]
        //                }
        //                //appearence: { closed: true,translucent:false }
        //            });
        //        }
                
        //        if (Tilescount == Result.d.length) {
        //            var LoadingTilesGIF = document.getElementById("TilesetLoading");
        //            var LoadingTilesLabel = document.getElementById("loadingTilesets");
        //            LoadingTilesLabel.style.display = 'none';
        //            LoadingTilesGIF.style.display = 'none';
        //        }
        //    }).otherwise(function (error) {
        //        throw (error);
        //    });

        //}
        //Add Elements to the dropdown list
        AddElementsToDropDown();
        //Add Elements to Dropdown2 list
        Render();
        Pageloaded = true;
        // HTML overlay for showing feature name on mouseover
        var nameOverlay = document.createElement('div');
        viewer.container.appendChild(nameOverlay);
        nameOverlay.className = 'backdrop';
        nameOverlay.style.display = 'none';
        nameOverlay.style.position = 'absolute';
        nameOverlay.style.bottom = '0';
        nameOverlay.style.left = '0';
        nameOverlay.style['pointer-events'] = 'none';
        nameOverlay.style.padding = '4px';
        nameOverlay.style.backgroundColor = 'black';
        nameOverlay.style.color = 'white';
        nameOverlay.style.content.bold();
        //nameOverlay.style.fontStyle.fontcolor = 'white';
        //nameOverlay.textContent.fontcolor = 'white';

        // Information about the currently selected feature
        var selected = {
            feature: undefined,
            originalColor: new Cesium.Color()
        };

        // An entity object which will hold info about the currently selected feature for infobox display
        var selectedEntity = new Cesium.Entity();

        // Get default left click handler for when a feature is not picked on left click
        var clickHandler = viewer.screenSpaceEventHandler.getInputAction(Cesium.ScreenSpaceEventType.LEFT_CLICK);

        // If silhouettes are supported, silhouette features in blue on mouse over and silhouette green on mouse click.
        // If silhouettes are not supported, change the feature color to yellow on mouse over and green on mouse click.
        if (Cesium.PostProcessStageLibrary.isSilhouetteSupported(viewer.scene)) {
            // Silhouettes are supported
            var silhouetteBlue = Cesium.PostProcessStageLibrary.createEdgeDetectionStage();
            silhouetteBlue.uniforms.color = Cesium.Color.BLUE;
            silhouetteBlue.uniforms.length = 0.01;
            silhouetteBlue.selected = [];

            var silhouetteGreen = Cesium.PostProcessStageLibrary.createEdgeDetectionStage();
            silhouetteGreen.uniforms.color = Cesium.Color.LIME;
            silhouetteGreen.uniforms.length = 0.01;
            silhouetteGreen.selected = [];

            viewer.scene.postProcessStages.add(Cesium.PostProcessStageLibrary.createSilhouetteStage([silhouetteBlue, silhouetteGreen]));

            // Silhouette a feature blue on hover.
            viewer.screenSpaceEventHandler.setInputAction(function onMouseMove(movement) {
                // If a feature was previously highlighted, undo the highlight
                silhouetteBlue.selected = [];

                // Pick a new feature
                var pickedFeature = viewer.scene.pick(movement.endPosition);
                if (!Cesium.defined(pickedFeature)) {
                    nameOverlay.style.display = 'none';
                    return;
                }
                // A feature was picked, so show it's overlay content
                nameOverlay.style.display = 'block';
                nameOverlay.style.bottom = viewer.canvas.clientHeight - movement.endPosition.y + 'px';
                nameOverlay.style.left = movement.endPosition.x + 'px';
                var name = pickedFeature.getProperty('citygml_measured_height');
                if (!Cesium.defined(name)) {
                    name = pickedFeature.getProperty('citygml_measured_height');
                }
                nameOverlay.textContent = " Height: " + name.toString();

                //nameOverlay.textContent.fontcolor = "white";
                // Highlight the feature if it's not already selected.
                if (pickedFeature !== selected.feature) {
                    silhouetteBlue.selected = [pickedFeature];
                }
            }, Cesium.ScreenSpaceEventType.MOUSE_MOVE);

            // Silhouette a feature on selection and show metadata in the InfoBox.
            viewer.screenSpaceEventHandler.setInputAction(function onLeftClick(movement) {
                // If a feature was previously selected, undo the highlight
                silhouetteGreen.selected = [];

                // Pick a new feature
                var pickedFeature = viewer.scene.pick(movement.position);
                if (!Cesium.defined(pickedFeature)) {
                    clickHandler(movement);
                    return;
                }

                // Select the feature if it's not already selected
                if (silhouetteGreen.selected[0] === pickedFeature) {
                    return;
                }

                // Save the selected feature's original color
                var highlightedFeature = silhouetteBlue.selected[0];
                if (pickedFeature === highlightedFeature) {
                    silhouetteBlue.selected = [];
                }

                // Highlight newly selected feature
                silhouetteGreen.selected = [pickedFeature];

                // Set feature infobox description
                var featureName = pickedFeature.getProperty('state');
                selectedEntity.name = featureName;
                selectedEntity.description = 'Loading <div class="cesium-infoBox-loading"></div>';
                viewer.selectedEntity = selectedEntity;
                selectedEntity.description = '<table class="cesium-infoBox-defaultTable"><tbody>' +
                                                '<tr><th>ObjectID</th><td>' + pickedFeature.getProperty('ubid') + '</td></tr>' +
                                                '<tr><th>Area (Sq.m)</th><td>' + parseFloat(pickedFeature.getProperty('area')).toFixed(2) + '</td></tr>' +
                                                '<tr><th>Height (m) </th><td>' + pickedFeature.getProperty('citygml_measured_height') + '</td></tr>' +
                                                '</tbody></table>';
            }, Cesium.ScreenSpaceEventType.LEFT_CLICK);
        } else {
            // Silhouettes are not supported. Instead, change the feature color.

            // Information about the currently highlighted feature
            var highlighted = {
                feature: undefined,
                originalColor: new Cesium.Color()
            };
        }

        var mainLoading = document.getElementById('main-loading');
        var appLoading = document.getElementById('app-loading');
        appLoading.style.display = 'none';
        mainLoading.style.display = 'none';
    }
    function OnError(Result) {
        alert(Result.responseText);
    }
    function OnFailed(Result) {
        alert("Failed");
    }
}
function ZoomToTile(Selected) {
    if (Pageloaded == true) {
        if (Selected.selectedIndex != 0) {
            for (var i = 0; i < Urls.length; i++) {
                
                if (Urls[i].Name == Selected.options[Selected.selectedIndex].text) {

                    scene.primitives.removeAll();

                    singleStateTilesCount = -1;

                    for (var j = 0; j < Urls[i].url.length; j++) {
                        var tileset = new Cesium.Cesium3DTileset({
                            url: "./" + Urls[i].url[j],
                        });
                        Tilescount += 1;
                        var TileSetName = Urls[i].url[j].toString();
                        TileSetName = TileSetName.split("/");
                        TileSetName = TileSetName[TileSetName.length - 4];

                        var stylingAttribute = "citygml_measured_height";

                        // adding center tile from the tileset against the state Name
                        AddingCenterTileset(tileset, TileSetName);

                        scene.primitives.add(tileset);

                        tileset.readyPromise.then(function (tileset) {

                            var properties = tileset.properties;

                            Alltiles.push({ Tileset: tileset });
                            //Alltiles[i].Tileset = tileset;
                            //var valuereq = tileset[0].properties;

                            if (Cesium.defined(properties) && Cesium.defined(properties[stylingAttribute])) {
                                tileset.style = new Cesium.Cesium3DTileStyle({
                                    color: {
                                        conditions: [
                                            ["${" + stylingAttribute + "} === null", "color('white')"],
                                            ["${" + stylingAttribute + "} >= 16", "color('maroon')"],
                                            ["${" + stylingAttribute + "} >= 12", "color('red')"],
                                            ["${" + stylingAttribute + "} >= 8", "color('yellow')"],
                                            ["${" + stylingAttribute + "} >= 5", "color('lightgreen')"],
                                            ["${" + stylingAttribute + "} >= 0", "color('blue')"],
                                            ["true", "color('gray')"]
                                        ]
                                    }
                                });
                            }

                        }).otherwise(function (error) {
                            throw (error);
                        });

                    }
                    break;
                }
            }
            
			var val = Selected.options[Selected.selectedIndex].value;
			
           viewer.flyTo(Urls[val].Tileset , { maximumHeight: 500, offset: { heading: 0, pitch: -45, range: 0.0 } });
			
		   
        }
    }
}
function SetStateNames(Result) {
    var PreviousState = "";
    //var j = -1;
    var z = -1;
    var urlcount = 0;
    for (var i = 0; i < Result.length; i++) {
        
        var nameofState = Result[i].toString();
        nameofState = nameofState.split("/");
        nameofState = nameofState[nameofState.length - 4];

        if (nameofState != PreviousState) {
            urlcount = 0;
            z += 1;
            Urls.push({Name:"",url:[],Tileset:null});
            Urls[z].Name = nameofState;
            Urls[z].url[urlcount] = Result[i];

        }
        else if (nameofState == PreviousState) {
            urlcount += 1;
            Urls[z].url[urlcount] = Result[i];
        }
        PreviousState = Urls[z].Name;
    }
}
function AddingCenterTileset(tileset, TileSetName) {
    singleStateTilesCount += 1;
    var CenterTile = 0;
    for (var i = 0; i < Urls.length; i++) {
        if (Urls[i].Name == TileSetName) {
            if (Urls[i].url.length % 2 == 0) {
                CenterTile = Urls[i].url.length / 2;
                if (CenterTile == singleStateTilesCount) {
                    Urls[i].Tileset = tileset;
                    break;
                }
            }
            else {
                CenterTile = ((Urls[i].url.length + 1) / 2)-1;
                if (CenterTile == singleStateTilesCount) {
                    Urls[i].Tileset = tileset;
                    break;
                }
            }
        }
    }
}
function AddElementsToDropDown() {

    var dropdown = document.getElementById("DropDown");
    var k = 0;
    for (var i = 0; i < Urls.length + 1; i++) {
        if (i == Urls.length) {
            var option = document.createElement('Option');
            option.text = "Zoom to State";
            option.value = "";
            dropdown.add(option, 0);
        }
        else {
            var option = document.createElement('Option');
            option.text = Urls[k].Name;
            option.value = k;
            dropdown.add(option, 0);
            k++;
        }
    }
    dropdown.selectedIndex = 0;
}
function Render() {
    var dropdown = document.getElementById("DropDown2");
    var option = document.createElement('Option');
    option.text = "Color by Area";
    option.value = "area";

    var option2 = document.createElement('Option');
    option2.text = "Color by Height";
    option2.value = "citygml_measured_height"

    dropdown.add(option2, 0);
    dropdown.add(option, 0);

}
function Symbology(Selected) {
    if (Pageloaded == true) {
        var stylingAttribute = Selected.options[Selected.selectedIndex].value;
        if (Alltiles.length > 0) {
            for (var i = 0; i < Alltiles.length; i++) {
                var properties = Alltiles[i].Tileset.properties;
                if (Cesium.defined(properties) && Cesium.defined(properties[stylingAttribute])) {
                    if (stylingAttribute == "citygml_measured_height") {
                        Alltiles[i].Tileset.style = new Cesium.Cesium3DTileStyle({
                            color: {
                                conditions: [
                                    ["${" + stylingAttribute + "} === null", "color('white')"],
                                    ["${" + stylingAttribute + "} >= 16", "color('maroon')"],
                                    ["${" + stylingAttribute + "} >= 12", "color('red')"],
                                    ["${" + stylingAttribute + "} >= 8", "color('yellow')"],
                                    ["${" + stylingAttribute + "} >= 5", "color('lightgreen')"],
                                    ["${" + stylingAttribute + "} >= 0", "color('blue')"],
                                    ["true", "color('gray')"]
                                ]
                            }
                        });
                        document.getElementById("AreaImage").style.visibility = "hidden";
                        document.getElementById("HeightImage").style.visibility = "visible";
                    }
                    if (stylingAttribute == "area") {
                        Alltiles[i].Tileset.style = new Cesium.Cesium3DTileStyle({
                            color: {
                                conditions: [
                                    ["Number(${" + stylingAttribute + "}) === null", "color('white')"],
                                    ["Number(${" + stylingAttribute + "}) >= 1000", "color('blue')"],
                                    ["Number(${" + stylingAttribute + "}) >= 500", "color('lightseagreen')"],
                                    ["Number(${" + stylingAttribute + "}) >= 200", "color('lightgreen')"],
                                    ["Number(${" + stylingAttribute + "}) >= 100", "color('yellow')"],
                                    ["Number(${" + stylingAttribute + "}) >= 20", "color('chocolate')"],
                                    ["Number(${" + stylingAttribute + "}) >= 10", "color('red')"],
                                    ["Number(${" + stylingAttribute + "}) >= 0", "color('maroon')"],
                                    ["true", "color('gray')"]
                                ]
                            }
                        });
                        document.getElementById("HeightImage").style.visibility = "hidden";
                        document.getElementById("AreaImage").style.visibility = "visible";
                    }
                }
            }
        }
    }
}
function AddLegend() {
    var table = document.getElementById("Legend");
    var tr = document.createElement("tr");
    var td = document.createElement("td");
    td.bgColor = "Blue";
    tr.add(td, 0);
    var td2 = document.createElement("td");
    td = "0";

}