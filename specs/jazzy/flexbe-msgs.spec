# Meta Package
Name:           ros-jazzy-flexbe-msgs
Version:        3.0.3
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/flexbe_msgs
Summary:        Meta package for ros2-jazzy-flexbe_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-flexbe_msgs
Requires:       ros2-jazzy-flexbe_msgs-devel

Obsoletes: ros-jazzy-flexbe-msgs < 3.0.3-1

%description
flexbe_msgs provides the messages used by FlexBE.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Tue Oct 15 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.3.0.3-1
- Update to latest release
