# Meta Package
Name:           ros-humble-camera-calibration-parsers
Version:        3.1.9
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/camera_calibration_parsers
Summary:        Meta package for ros2-humble-camera_calibration_parsers and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-camera_calibration_parsers
Requires:       ros2-humble-camera_calibration_parsers-devel

Obsoletes: ros-humble-camera-calibration-parsers < 3.1.9-1

%description
camera_calibration_parsers contains routines for reading and writing
camera calibration parameters.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Aug 12 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.3.1.9-1
- Update to latest release
