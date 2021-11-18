
import React from 'react'
import { StyleSheet, Dimensions } from 'react-native'
var { height, width } = Dimensions.get('window')

const styles = StyleSheet.create(

    {
        body: {
            flex:1,
            backgroundColor:'#0080FF',
            fontSize:'14'
        },
        container: {
            marginTop: 0.1 * height,
            backgroundColor: '#0080FF'

        },
        button: {
            flex:1,
            backgroundColor: '#08298A',
            justifyContent: 'center',
            alignItems: 'center',
            borderRadius: 5,
            marginHorizontal: 0.02 * width,
            marginVertical: 0.01 * height,
            height: 0.1 * height
        },
        row: {
            flexDirection: 'row'
        },
        screen: {
            flex: 1,
            backgroundColor: "white",
            borderRadius: 5,
            marginHorizontal: 0.02 * width,
            height: 0.2 * height,
            textAlign: 'right',
            fontSize: 20,
            paddingRight: 10,
            marginBottom: 0.05 * height

        }
    }
)
export {styles}