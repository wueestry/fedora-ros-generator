# Meta Package
Name:           ros-iron-backward-ros
Version:        1.0.2
Release:        1%{?dist}
License:        MIT
URL:            http://www.ros.org/
Summary:        Meta package for ros2-iron-backward_ros and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-iron-backward_ros
Requires:       ros2-iron-backward_ros-devel

Obsoletes: ros-iron-backward-ros < 1.0.2-1

%description
The backward_ros package is a ros wrapper of backward-cpp from
https://github.com/bombela/backward-cpp

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri Apr 26 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - iron.1.0.2-1
- Update to latest release
