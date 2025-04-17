# Meta Package
Name:           ros-jazzy-camera-info-manager
Version:        5.1.6
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/camera_info_manager
Summary:        Meta package for ros2-jazzy-camera_info_manager and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-camera_info_manager
Requires:       ros2-jazzy-camera_info_manager-devel

Obsoletes: ros-jazzy-camera-info-manager < 5.1.6-1

%description
This package provides a C++ interface for camera calibration
information. It provides CameraInfo, and handles SetCameraInfo service
requests, saving and restoring the camera calibration data.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Thu Apr 10 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.5.1.6-1
- Update to latest release
* Mon Jan 13 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.5.1.5-1
- Update to latest release
* Sat Aug 03 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.5.1.4-1
- Update to latest release
