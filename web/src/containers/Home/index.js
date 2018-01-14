// @flow
import React, { Component, PropTypes } from 'react';
import { connect } from 'react-redux';
import { css, StyleSheet } from 'aphrodite';
import { fetchCameras, createCamera } from '../../actions/cameras';
import NewCameraForm from '../../components/NewCameraForm';
import Navbar from '../../components/Navbar';
import CameraListItem from '../../components/CameraListItem';
import Radar from 'react-d3-radar';

const styles = StyleSheet.create({
  card: {
    maxWidth: '500px',
    padding: '3rem 4rem',
    margin: '2rem auto',
  },
});

type Camera = {
  id: number,
  name: string,
}

type Props = {
  cameras: Array<Camera>,
  currentCameras: Array<Camera>,
  fetchCameras: () => void,
  createCamera: () => void
}

class Home extends Component {
  static contextTypes = {
    router: PropTypes.object,
  }

  componentDidMount() {
    this.props.fetchCameras(this.props.user);
  }

  props: Props

  handleNewCameraSubmit = data => this.props.createCamera(data, this.props.user, this.context.router);

  renderCameras() {
    const currentCameraIds = [];
    this.props.currentCameras.map(camera => currentCameraIds.push(camera.id));

    return this.props.cameras.map(camera =>
      <CameraListItem
        key={camera.id}
        camera={camera}
        currentCameraIds={currentCameraIds}
      />
    );
  }

  render() {
    return (
      <div style={{ flex: '1' }}>
        <Navbar />
        <div className={`card ${css(styles.card)}`}>
          <h3 style={{ marginBottom: '2rem', textAlign: 'center' }}>Add a camera</h3>
          <NewCameraForm onSubmit={this.handleNewCameraSubmit} />
        </div>
        <div className={`card ${css(styles.card)}`}>
          <h3 style={{ marginBottom: '2rem', textAlign: 'center' }}>Your current statistics</h3>
          <Radar
  width={450}
  height={450}
  padding={50}
  domainMax={10}
  highlighted={null}
  onHover={(point) => {
    if (point) {
      console.log('hovered over a data point');
    } else {
      console.log('not over anything');
    }
  }}
  data={{
    variables: [
      {key: 'anger', label: 'Anger'},
      {key: 'disgusted', label: 'Disgusted'},
      {key: 'fearful', label: 'Fearful'},
      {key: 'happy', label: 'Happy'},
      {key: 'sad', label: 'Sad'},
      {key: 'surprised', label: 'Surprised'},
      {key: 'neutral', label: 'Neutral'},
    ],
    sets: [
      {
        key: 'today',
        label: 'today',
        values: {
          anger: 4,
          disgusted: 6,
          fearful: 7,
          happy: 2,
          sad: 8,
          surprised: 1,
          neutral: 2,
        },
      },
      {
        key: 'weekly',
        label: 'weekly',
        values: {
          anger: 10,
          disgusted: 8,
          fearful: 6,
          happy: 4,
          sad: 2,
          surprised: 0,
          neutral: 5,
        },
      },
    ],
  }}
/>
        </div>
      </div>
    );
  }
}

export default connect(
  state => ({
    user: state.session.currentUser,
    cameras: state.cameras.all,
    currentCameras: state.cameras.currentCameras,
  }),
  { fetchCameras, createCamera }
)(Home);
