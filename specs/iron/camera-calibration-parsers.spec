# Meta Package
Name:           ros-iron-camera-calibration-parsers
Version:        4.2.4
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/camera_calibration_parsers
Summary:        Meta package for ros2-iron-camera_calibration_parsers and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-camera_calibration_parsers
Requires:       ros2-iron-camera_calibration_parsers-devel

Obsoletes: ros-iron-camera-calibration-parsers < 4.2.4-1

%description
camera_calibration_parsers contains routines for reading and writing
camera calibration parameters.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.4.2.4-1
- Update to latest release
