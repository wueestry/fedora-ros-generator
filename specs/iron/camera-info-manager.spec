# Meta Package
Name:           ros-iron-camera-info-manager
Version:        4.2.4
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/camera_info_manager
Summary:        Meta package for ros2-iron-camera_info_manager and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-camera_info_manager
Requires:       ros2-iron-camera_info_manager-devel

Obsoletes: ros-iron-camera-info-manager < 4.2.4-1

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
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.4.2.4-1
- Update to latest release
