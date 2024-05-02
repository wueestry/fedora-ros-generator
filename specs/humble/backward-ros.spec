# Meta Package
Name:           ros-humble-backward-ros
Version:        1.0.2
Release:        1%{?dist}
License:        MIT
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-backward_ros and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-backward_ros
Requires:       ros2-humble-backward_ros-devel

Obsoletes: ros-humble-backward-ros < 1.0.2-1

%description
The backward_ros package is a ros wrapper of backward-cpp from
https://github.com/bombela/backward-cpp

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.0.2-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.0.2-1
- update to latest upstream release
* Thu Mar 09 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.1.0.2-1
- Initial humble build
