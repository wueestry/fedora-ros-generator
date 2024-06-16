# Meta Package
Name:           ros-humble-stereo-msgs
Version:        4.2.4
Release:        1%{?dist}
License:        Apache License 2.0
URL:            http://www.ros.org/
Summary:        Meta package for ros2-humble-stereo_msgs and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-stereo_msgs
Requires:       ros2-humble-stereo_msgs-devel

Obsoletes: ros-humble-stereo-msgs < 4.2.4-1

%description
A package containing some stereo camera related message definitions.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Fri May 24 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.4.2.4-1
- Update to latest release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.4.2.3-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.4.2.3-1
- update to latest upstream release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.4.2.3-1
- update to latest release
* Mon Mar 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - noetic.1.13.1-1
- update to latest release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.4.2.3-1
- Initial humble build
