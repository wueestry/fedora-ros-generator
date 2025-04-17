# Meta Package
Name:           ros-jazzy-backward-ros
Version:        1.0.7
Release:        1%{?dist}
License:        MIT
URL:            https://github.com/pal-robotics/backward_ros
Summary:        Meta package for ros2-jazzy-backward_ros and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-jazzy-backward_ros
Requires:       ros2-jazzy-backward_ros-devel

Obsoletes: ros-jazzy-backward-ros < 1.0.7-1

%description
The backward_ros package is a ros wrapper of backward-cpp from
https://github.com/bombela/backward-cpp

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Sat Mar 08 2025 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.0.7-1
- Update to latest release
* Wed Nov 20 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.0.6-1
- Update to latest release
* Thu Jul 11 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.0.5-1
- Update to latest release
* Sat Apr 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - jazzy.1.0.2-1
- Update to latest release
