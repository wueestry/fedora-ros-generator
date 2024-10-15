# Meta Package
Name:           ros-jazzy-camera-calibration
Version:        5.0.4
Release:        1%{?dist}
License:        BSD
URL:            https://index.ros.org/p/camera_calibration/github-ros-perception-image_pipeline/
Summary:        Meta package for ros2-jazzy-camera_calibration and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-camera_calibration
Requires:       ros2-jazzy-camera_calibration-devel

Obsoletes: ros-jazzy-camera-calibration < 5.0.4-1

%description
camera_calibration allows easy calibration of monocular or stereo
cameras using a checkerboard calibration target.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Aug 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.5.0.4-1
- Update to latest release
* Sat Aug 03 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.5.0.3-1
- Update to latest release
