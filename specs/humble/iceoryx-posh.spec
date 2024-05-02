# Meta Package
Name:           ros-humble-iceoryx-posh
Version:        2.0.5
Release:        1%{?dist}
License:        Apache 2.0
URL:            https://iceoryx.io
Summary:        Meta package for ros2-humble-iceoryx_posh and its development package to adhere to ubuntu pkg names
BuildArch: noarch

Requires:       ros2-humble-iceoryx_posh
Requires:       ros2-humble-iceoryx_posh-devel

Obsoletes: ros-humble-iceoryx-posh < 2.0.5-1

%description
Eclipse iceoryx inter-process-communication (IPC) middleware Posix
Shared Memory Library and middleware daemon (RouDi)

%build

%clean
rm -rf $RPM_BUILD_ROOT

%install

%files

%changelog
* Wed Dec 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.0.5-1
- update to latest upstream
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.0.3-1
- update to latest upstream release
* Wed Aug 23 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.0.3-1
- update to latest upstream release
* Mon Mar 06 2023 Tarik Viehmann <viehmann@kbsg.rwth-aachen.de> - humble.2.0.3-1
- Initial humble build
