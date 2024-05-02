# Meta Package
Name:           ros-humble-octomap-msgs
Version:        2.0.0
Release:        1%{?dist}
License:        BSD
URL:            http://ros.org/wiki/octomap_msgs
Summary:        Meta package for ros2-humble-octomap_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-octomap_msgs
Requires:       ros2-humble-octomap_msgs-devel

Obsoletes: ros-humble-octomap-msgs < 2.0.0-1

%description
This package provides messages and serializations / conversion for the

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Sep 27 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.0.0-1
- update to latest release
* Thu Mar 09 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.0.0-1
- Initial humble build
