# Meta Package
Name:           ros-jazzy-camera-calibration-parsers
Version:        5.1.4
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/camera_calibration_parsers
Summary:        Meta package for ros2-jazzy-camera_calibration_parsers and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-camera_calibration_parsers
Requires:       ros2-jazzy-camera_calibration_parsers-devel

Obsoletes: ros-jazzy-camera-calibration-parsers < 5.1.4-1

%description
camera_calibration_parsers contains routines for reading and writing
camera calibration parameters.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Aug 03 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.5.1.4-1
- Update to latest release
