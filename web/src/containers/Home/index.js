// @flow
import React, { Component, PropTypes } from 'react';
import { connect } from 'react-redux';
import { css, StyleSheet } from 'aphrodite';
import { fetchCameras, createCamera } from '../../actions/cameras';
import NewCameraForm from '../../components/NewCameraForm';
import Navbar from '../../components/Navbar';
import CameraListItem from '../../components/CameraListItem';

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

  handleNewCameraSubmit = data => this.props.createCamera(data, this.context.router);

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
          <h3 style={{ marginBottom: '2rem', textAlign: 'center' }}>Your favourite minds:</h3>
          {/* {this.renderSomethins()} */}
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
