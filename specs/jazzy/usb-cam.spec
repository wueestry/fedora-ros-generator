# Meta Package
Name:           ros-jazzy-usb-cam
Version:        0.8.1
Release:        1%{?dist}
License:        BSD
URL:            http://wiki.ros.org/usb_cam
Summary:        Meta package for ros2-jazzy-usb_cam and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-usb_cam
Requires:       ros2-jazzy-usb_cam-devel

Obsoletes: ros-jazzy-usb-cam < 0.8.1-1

%description
A ROS Driver for V4L USB Cameras

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Mar 14 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.0.8.1-1
- Update to latest release
