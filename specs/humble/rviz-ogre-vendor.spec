# Meta Package
Name:           ros-humble-rviz-ogre-vendor
Version:        11.2.13
Release:        1%{?dist}
License:        Apache License 2.0
URL:            https://www.ogre3d.org/
Summary:        Meta package for ros2-humble-rviz_ogre_vendor and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-rviz_ogre_vendor
Requires:       ros2-humble-rviz_ogre_vendor-devel

Obsoletes: ros-humble-rviz-ogre-vendor < 11.2.13-1

%description
Wrapper around ogre3d, it provides a fixed CMake module and an
ExternalProject build of ogre.

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Mon Aug 12 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.11.2.13-1
- Update to latest release
* Wed Mar 27 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.11.2.12-1
- update to latest release
* Mon Feb 19 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.11.2.11-1
- Update to latest release
* Sat Feb 10 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.11.2.10-2
- update ogre minor version
* Sat Feb 10 2024 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.11.2.10-1
- Add Ogre EGL support
* Wed Dec 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.11.2.9-1
- update to latest upstream
* Wed Sep 27 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.11.2.8-1
- update to latest release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.11.2.7-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.11.2.7-1
- update to latest upstream release
* Tue Aug 08 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.11.2.7-1
- update to latest upstream
* Thu Jul 20 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.11.2.6-1
- update to latest release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.11.2.5-1
- Initial humble build
