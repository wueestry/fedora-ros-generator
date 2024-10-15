# Meta Package
Name:           ros-humble-camera-calibration
Version:        3.0.5
Release:        1%{?dist}
License:        BSD
URL:            https://index.ros.org/p/camera_calibration/github-ros-perception-image_pipeline/
Summary:        Meta package for ros2-humble-camera_calibration and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-camera_calibration
Requires:       ros2-humble-camera_calibration-devel

Obsoletes: ros-humble-camera-calibration < 3.0.5-1

%description
camera_calibration allows easy calibration of monocular or stereo
cameras using a checkerboard calibration target.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Aug 12 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.0.5-1
- Update to latest release
